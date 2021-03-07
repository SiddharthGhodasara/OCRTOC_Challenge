#! /usr/bin/env python

#Importing Libraries
import os
import tf
import cv2
import math
import time
import rospy
import rospkg
import tf2_ros
import numpy as np
import open3d as o3d
import geometry_msgs.msg
import tf2_geometry_msgs
from PIL import Image as img
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel


import open3d 
import open3d as o3d
import numpy as np
from ctypes import * # convert float to uint32
import message_filters
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import copy
import tf 
import time
from tf.transformations import * 
import math
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import *

#Getting the parameters from launch file
#print(rospy.get_param_names())
image_topic = rospy.get_param("/image_topic")
camera_topic = rospy.get_param('/camera_topic')
depth_topic = rospy.get_param('/depth_topic')
camera_frame = rospy.get_param('/camera_frame')

#Defining global variables
focal_length = None
center = None
camera_matrix = None
dist_coeffs = np.zeros((4,1))

print("Image topic is", image_topic)

#Defining the bridge
bridge = CvBridge()

#Declaring the publisher
pub = None
#Defining camera info global varibale
camera_info = None
cam_model = None
#Storing the depth
depth = None

voxel_size = 0.005

#Tranform Listener
tf_listener = None
#Transformations
tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length

#Loading the labels
rospack = rospkg.RosPack()
package_path = rospack.get_path('3D_Pose_Estimation')
labelsPath = os.path.sep.join([package_path, 'yolo', 'obj.names'])
LABELS = open(labelsPath).read().strip().split("\n")

#Derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny.weights"])
configPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny.cfg"])

# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


def transform_frames():
	listener = tf.TransformListener()
	rospy.sleep(2)
	trans1,quat1 =listener.lookupTransform("world","kinect_optical_frame",rospy.Time())

	htm1 = tf.transformations.quaternion_matrix(quat1)

	for i in range(0,3):
		htm1[i][3] = trans1[i]

	return htm1


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    #source_temp.paint_uniform_color([1, 0.706, 0])
    #target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp]) # ,zoom=0.4559,front=[0.6452, -0.3036, -0.7011],lookat=[1.9892, 2.0208, 1.8945],up=[-0.2779, -0.9482, 0.1556])

def preprocess_point_cloud(pcd, voxel_size):
    print(":: Downsample with a voxel size %.3f." % voxel_size)
    pcd_down =  o3d.geometry.voxel_down_sample(pcd, voxel_size)

    radius_normal = voxel_size * 2
    print(":: Estimate normal with search radius %.3f." % radius_normal)
    o3d.geometry.estimate_normals(pcd_down,o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = voxel_size * 5
    print(":: Compute FPFH feature with search radius %.3f." % radius_feature)
    pcd_fpfh = o3d.registration.compute_fpfh_feature(pcd_down,o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return pcd_down, pcd_fpfh


def execute_global_registration(source_down, target_down, source_fpfh,
                                target_fpfh, voxel_size):
    distance_threshold = voxel_size * 1.5
    print(":: RANSAC registration on downsampled point clouds.")
    print("   Since the downsampling voxel size is %.3f," % voxel_size)
    print("   we use a liberal distance threshold %.3f." % distance_threshold)
    result = o3d.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, distance_threshold,
        o3d.registration.TransformationEstimationPointToPoint(False),
        4, [
            o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(
                0.9),
            o3d.registration.CorrespondenceCheckerBasedOnDistance(
                distance_threshold)
        ], o3d.registration.RANSACConvergenceCriteria(4000000, 500))
    return result


def htm_to_transform(matrix):
    #Extracting the rotation matrix
    rotation_mat = np.eye(4)
    rotation_mat[:3,:3] = ((matrix[0][0], matrix[0][1], matrix[0][2]),(matrix[1][0], matrix[1][1], matrix[1][2]),(matrix[2][0], matrix[2][1], matrix[2][2]))
    #m[:3,:3] = ((a, b, c), (d, e, f), (g, h, i))
    translation_vec = np.array([matrix[0][3], matrix[1][3], matrix[2][3]])

    euler = tf.transformations.euler_from_matrix(rotation_mat)
    #print(translation_vec)
    #out = transform(translation_vec[0], translation_vec[1], translation_vec[2], euler[0], euler[1], euler[2], euler[3])
    #print(euler)
    return translation_vec, euler, rotation_mat

def refine_registration(source, target, source_fpfh, target_fpfh, voxel_size, transformation):
    distance_threshold = voxel_size * 0.4
    print(":: Point-to-plane ICP registration is applied on original point")
    print("   clouds to refine the alignment. This time we use a strict")
    print("   distance threshold %.3f." % distance_threshold)
    result = o3d.registration.registration_icp(source, target, distance_threshold,transformation,
        o3d.registration.TransformationEstimationPointToPlane())
    return result


def prepare_dataset(source, target, voxel_size, transform):
    print(":: Load two point clouds and disturb initial pose.")
    #init = o3d.io.read_point_cloud("/home/gaurav/object.pcd")
    #source = o3d.io.read_point_cloud("/home/gaurav/PCD/jenga.pcd") #/home/kaushik/Open3D/examples/test_data/ICP/cloud_bin_0.pcd
    #target = o3d.io.read_point_cloud("/home/gaurav/PCD/1-138_initial.pcd") #/home/kaushik/object2.pcd
    
                     
    #source.transform(transform)
    target.transform(transform)

    #draw_registration_result(source, target, np.identity(4))
    o3d.visualization.draw_geometries([source,target])
    source_down, source_fpfh = preprocess_point_cloud(source, voxel_size)
    target_down, target_fpfh = preprocess_point_cloud(target, voxel_size)
    return source, target, source_down, target_down, source_fpfh, target_fpfh


#Function for converting coordinates to base link frame
def uv_to_xyz(cx, cy):
    #Converting to XYZ coordinates
    (x, y, z) = cam_model.projectPixelTo3dRay((cx, cy))
    #Normalising
    x = x/z
    y = y/z
    z = z/z

    #Getting the depth at given coordinates
    depth = rospy.wait_for_message(depth_topic, Image)
    depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
    lookup = depth_img.load()
    d = lookup[cx, cy]

    #Modifying the coordinates
    x *= d
    y *= d
    z *= d

    #Making Point Stamp Message
    grasp_pose = geometry_msgs.msg.PointStamped()
    grasp_pose.header.frame_id = camera_frame
    point = geometry_msgs.msg.Point()
    grasp_pose.point.x =  x
    grasp_pose.point.y =  y
    grasp_pose.point.z =  z

    #Transforming
    target_frame = "world"
    source_frame = camera_frame
    transform = tf_buffer.lookup_transform(target_frame,
                                           source_frame, #source frame
                                           rospy.Time(0), #get the tf at first available time
                                           rospy.Duration(1.0)) #wait for 1 second

    #Applying the transform
    pose_transformed = tf2_geometry_msgs.do_transform_point(grasp_pose, transform)
    #Returning the transform coordinates
    return pose_transformed

#Prediction Function
def prediction(image):
    #Getting the image dimensions
    (H, W) = image.shape[:2]

    global focal_length
    global center
    global camera_matrix

    center = (W/2, H/2)
    focal_length = center[0] / np.tan(60/2 * np.pi / 180)
    camera_matrix = np.array([[focal_length, 0, center[0]],
                            [0, focal_length, center[1]],
                            [0, 0, 1]], dtype = "double")

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    #Creating Blob from images
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    #Feeding the blob as input
    net.setInput(blob)
    #Forward pass
    layerOutputs = net.forward(ln)

    #Initializing lists of Detected Bounding Boxes, Confidences, and Class IDs
    boxes = []
    confidences = []
    classIDs = []

    #Looping over each of the layer outputs
    for output in layerOutputs:
    	#Looping over each of the detections
    	for detection in output:
    		#Extracting the class ID and confidence
    		scores = detection[5:]
    		classID = np.argmax(scores)
    		confidence = scores[classID]

            #Filtering out weak predictions
    		if confidence > 0.5:
    			#Scale the Bounding Box Coordinates
    			box = detection[0:4] * np.array([W, H, W, H])
    			(centerX, centerY, width, height) = box.astype("int")
                # use the center (x, y)-coordinates to derive the top and
    			# and left corner of the bounding box
    			x = int(centerX - (width / 2))
    			y = int(centerY - (height / 2))
                #Updating the Lists
    			boxes.append([x, y, int(width), int(height)])
    			confidences.append(float(confidence))
    			classIDs.append(classID)

    #Applying non-max Suppression
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

    #Ensuring at least one detection exists
    if len(idxs) > 0:
    	#Looping over the indexes
        print(len(idxs))
        label_str = ""
    	for i in idxs.flatten():
            #Extracting the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            #Getting the labels
            label = LABELS[classIDs[i]]

            #Getting center coordinates
            cx = x + (w/2)
            cy = y + (h/2)

            #Converting the center cooridnates to base link frame
            xy_pose = uv_to_xyz(cx, cy)

            #Comupting Initial Transformation Matrix
            trans_init = np.array([[1.0, 0.0, 0.0, xy_pose.point.x], [0.0, 1.0, 0.0, xy_pose.point.y], [0.0, 0.0, 1.0, xy_pose.point.z], [0.0, 0.0, 0.0, 1.0]])

            #Extracting the bounding box image
            box_img = image[y-10 : y+h+10, x-10 : x+w+10]
            
            #Converting to RGB Color Space
            box_img = cv2.cvtColor(box_img, cv2.COLOR_BGR2RGB)

            #Getting the depth image
            depth = rospy.wait_for_message(depth_topic, Image)
            
            #Converting to cv2 image from sensor_msg image
            try:
                dpeth_converted = bridge.imgmsg_to_cv2(depth, desired_encoding='passthrough')
            except CvBridgeError, e:
                print e

            #Converting to np array
            depth_array = np.array(dpeth_converted)

            #Extracting the depth image of the bounding box
            depth_box = depth_array[y-10 : y+h+10, x-10 : x+w+10]

            #Generating open3D RGBD Image
            o3d_rgbd = o3d.geometry.RGBDImage()
            o3d_rgbd_color = o3d.geometry.Image(box_img)
            o3d_rgbd_depth = o3d.geometry.Image(depth_box.astype(np.float32))
            o3d_rgbd.color = o3d_rgbd_color
            o3d_rgbd.depth = o3d_rgbd_depth
            
            #Computing Intrinsic Parameters of Camera
            intrinsic = o3d.camera.PinholeCameraIntrinsic()
            (H, W) = image.shape[:2]
            center_x = 640.5
            center_y = 360.5
            focal_length_y = 1120.1199067175087
            focal_length_x = 1120.1199067175087
            intrinsic.set_intrinsics(W, H, focal_length_x, focal_length_y, center_x, center_y)

            #Generating Point Cloud from RGBD Image
            pcd = o3d.geometry.create_point_cloud_from_rgbd_image(o3d_rgbd, intrinsic)

            if label == 'potted_meat_can':
                #Reading the source comprasion file
                s = o3d.io.read_point_cloud("/home/kaushik/PCD/potted_meat_can_mesh.pcd")

                #Preprcoessing the point clouds
                source, target, source_down, target_down, source_fpfh, target_fpfh = prepare_dataset(s, pcd, voxel_size, transform_frames())

                #Global Registration
                result_ransac = execute_global_registration(source_down, target_down,source_fpfh, target_fpfh,voxel_size)

                #Local Refinement
                result_icp = refine_registration(source_down, target_down, source_fpfh, target_fpfh,voxel_size,result_ransac.transformation)

                #Visualization
                draw_registration_result(source, target, result_icp.transformation)

                #Computing total tranformation
                #total_trans = result_icp.transformation * trans_init
                trans_vec, euler, rot_mat = htm_to_transform(result_ransac.transformation)
                trans_vec_, _, rot_mat_ = htm_to_transform(trans_init)
                trans_vec_total = trans_vec + trans_vec_
                rot_mat_total = rot_mat * rot_mat_
                euler_total = tf.transformations.euler_from_matrix(rot_mat_total)
                
                #print("ICP Transformation - ", htm_to_transform(result_icp.transformation))
                #print("Total Transformation - \n ", htm_to_transform(total_trans))
                print(trans_vec_)
                print(euler)
                print("Accuracy - ", (result_ransac.fitness + confidences[i])/2)

            else:
                print(label)


        #Checking if subscribers are present
        while pub.get_num_connections() < 1:
			None
        #Publishing
        pub.publish(label_str)
        print("Published")





#Image Callback Function
def callback(data):
    try:
        #Converting Sensor Image to cv2 Image
        cv_img = bridge.imgmsg_to_cv2(data, 'bgr8')
        #Calling the prediction function
        prediction(cv_img)
    #Handling exceptions
    except CvBridgeError as e:
        print(e)
transform = None
#Main Function
def main():
    #Defining global variable usage
    global pub
    global cam_model
    global tf_listener
    global transform
    #Initialising the node
    rospy.init_node("object_detection")


    #Getting camera info
    camera_info = rospy.wait_for_message(camera_topic, CameraInfo)
    #Setting up Camera Model
    cam_model = PinholeCameraModel()
    cam_model.fromCameraInfo(camera_info)

    #Initialising Transformations
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    #Initialising the publisher
    pub = rospy.Publisher('/pose', String, queue_size = 10)
    #Subscribinig to image topic
    sub = rospy.Subscriber(image_topic, Image, callback)

    #Stopping the node from termination
    rospy.spin()

#Calling the main thread
if __name__ == "__main__":
    main()
