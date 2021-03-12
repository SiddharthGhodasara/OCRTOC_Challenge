#! /usr/bin/env python

#Importing Libraries
import tf
import cv2
import copy
import rospy
import numpy as np
import open3d as o3d
import message_filters
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import sensor_msgs.point_cloud2 as pc2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import PointCloud2, PointField

#Defining the bridge
bridge = CvBridge()
pcd_pub = None

#Function to convert O3D PointCloud to ROS PointCloud2
def convertCloudFromOpen3dToRos(open3d_cloud, frame_id="realsense_link"):

    # The data structure of each point in ros PointCloud2: 16 bits = x + y + z + rgb
    FIELDS_XYZ = [
        PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
        PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
        PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
    ]
    FIELDS_XYZRGB = FIELDS_XYZ + \
        [PointField(name='rgb', offset=12, datatype=PointField.UINT32, count=1)]

    # Bit operations
    BIT_MOVE_16 = 2**16
    BIT_MOVE_8 = 2**8

    # Set "header"
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = frame_id

    # Set "fields" and "cloud_data"
    points = np.asarray(open3d_cloud.points)
    # XYZ only
    if not open3d_cloud.colors: 
        fields=FIELDS_XYZ
        cloud_data=points

    # XYZ + RGB
    else: 
        fields=FIELDS_XYZRGB
        # -- Change rgb color from "three float" to "one 24-byte int" 0x00FFFFFF is white, 0x00000000 is black.
        colors = np.floor(np.asarray(open3d_cloud.colors)*255) # nx3 matrix
        colors = colors[:,0] * BIT_MOVE_16 +colors[:,1] * BIT_MOVE_8 + colors[:,2]  
        cloud_data=np.c_[points, colors]
    
    # create ros_cloud
    return pc2.create_cloud(header, fields, cloud_data)


#Callback Function
def callback(rgb_img, depth_img):
    #Converting sensor_msg image to cv image
    try:
        cv_img = bridge.imgmsg_to_cv2(rgb_img, 'rgb8')
        depth_converted = bridge.imgmsg_to_cv2(depth_img, desired_encoding='passthrough')

    except CvBridgeError as e:
        print(e)
    
    print(cv_img.shape)
    print(depth_converted.shape)
    #Making Images to generate RGBD Image
    o3d_rgbd_color = o3d.geometry.Image(cv_img)
    o3d_rgbd_depth = o3d.geometry.Image(depth_converted.astype(np.float32))

    #Generating open3D RGBD Image
    o3d_rgbd = o3d.geometry.RGBDImage()
    o3d_rgbd.color = o3d_rgbd_color
    o3d_rgbd.depth = o3d_rgbd_depth

    #Computing Intrinsic Parameters of Camera
    intrinsic = o3d.camera.PinholeCameraIntrinsic()
    (H, W) = cv_img.shape[:2]
    center_x = 317.130859375
    center_y = 239.40304565429688
    focal_length_y = 607.8826293945312
    focal_length_x = 607.946044921875
    intrinsic.set_intrinsics(W, H, focal_length_x, focal_length_y, center_x, center_y)

    #Generating Point Cloud from RGBD Image
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(o3d_rgbd, intrinsic)

    #Visualizing
    #o3d.visualization.draw_geometries([pcd])

    #Converting O3D Point Cloud to PointCloud2
    ros_pcd = convertCloudFromOpen3dToRos(pcd)

    #Publishing
    pcd_pub.publish(ros_pcd)


# Main Thread
if __name__ == "__main__":
    
    #Initialising the node
    rospy.init_node("rs_rgbd_pointcloud")

    #Defining the Publisher
    global pcd_pub
    pcd_pub = rospy.Publisher('/rs_rgbd', PointCloud2, queue_size = 10)

    #Subscribing to syncronized RGB and Depth Image
    rgb_sub = message_filters.Subscriber('/realsense/color/image_raw', Image)
    depth_sub = message_filters.Subscriber('/realsense/depth/image_rect_raw', Image)
    ts = message_filters.TimeSynchronizer([rgb_sub, depth_sub], 10)
    ts.registerCallback(callback)

    rospy.spin()
