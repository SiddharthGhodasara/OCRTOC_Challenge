#!/usr/bin/env python
import open3d 
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
convert_rgbUint32_to_tuple = lambda rgb_uint32: (
	(rgb_uint32 & 0x00ff0000)>>16, (rgb_uint32 & 0x0000ff00)>>8, (rgb_uint32 & 0x000000ff)
)
convert_rgbFloat_to_tuple = lambda rgb_float: convert_rgbUint32_to_tuple(
	int(cast(pointer(c_float(rgb_float)), POINTER(c_uint32)).contents.value)
)


def convertCloudFromRosToOpen3d(ros_cloud):
	
	# Get cloud data from ros_cloud
	field_names=[field.name for field in ros_cloud.fields]
	cloud_data = list(pc2.read_points(ros_cloud, skip_nans=True, field_names = field_names))

	# Check empty
	open3d_cloud = open3d.PointCloud()
	if len(cloud_data)==0:
		print("Converting an empty cloud")
		return None

	# Set open3d_cloud
	if "rgb" in field_names:
		IDX_RGB_IN_FIELD=3 # x, y, z, rgb
		
		# Get xyz
		xyz = [(x,y,z) for x,y,z,rgb in cloud_data ] # (why cannot put this line below rgb?)

		# Get rgb
		# Check whether int or float
		if type(cloud_data[0][IDX_RGB_IN_FIELD])==float: # if float (from pcl::toROSMsg)
			rgb = [convert_rgbFloat_to_tuple(rgb) for x,y,z,rgb in cloud_data ]
		else:
			rgb = [convert_rgbUint32_to_tuple(rgb) for x,y,z,rgb in cloud_data ]

		# combine
		open3d_cloud.points = open3d.Vector3dVector(np.array(xyz))
		open3d_cloud.colors = open3d.Vector3dVector(np.array(rgb)/255.0)
	else:
		xyz = [(x,y,z) for x,y,z in cloud_data ] # get xyz
		open3d_cloud.points = open3d.Vector3dVector(np.array(xyz))

	return open3d_cloud
	# draw geometry
	open3d.draw_geometries([open3d_cloud])

def convertCloudFromOpen3dToRos(open3d_cloud, frame_id="world"):
    # Set "header"
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = frame_id

    # Set "fields" and "cloud_data"
    points=np.asarray(open3d_cloud.points)
    if not open3d_cloud.colors: # XYZ only
        fields=FIELDS_XYZ
        cloud_data=points
    else: # XYZ + RGB
        fields=FIELDS_XYZRGB
        # -- Change rgb color from "three float" to "one 24-byte int"
        # 0x00FFFFFF is white, 0x00000000 is black.
        colors = np.floor(np.asarray(open3d_cloud.colors)*255) # nx3 matrix
        colors = colors[:,0] * BIT_MOVE_16 +colors[:,1] * BIT_MOVE_8 + colors[:,2]  
        cloud_data=np.c_[points, colors]
    
    # create ros_cloud
    return pc2.create_cloud(header, fields, cloud_data)

def publish_cloud(open3d_cloud):
    while not rospy.is_shutdown():
		rospy.loginfo("-- Not receiving ROS PointCloud2 message yet ...")

		if 1: # Use the cloud from file
			rospy.loginfo("Converting cloud from Open3d to ROS PointCloud2 ...")
			ros_cloud = convertCloudFromOpen3dToRos(open3d_cloud)

		else: # Use the cloud with 3 points generated below
			rospy.loginfo("Converting a 3-point cloud into ROS PointCloud2 ...")
			TEST_CLOUD_POINTS = [
				[1.0, 0.0, 0.0, 0xff0000],
				[0.0, 1.0, 0.0, 0x00ff00],
				[0.0, 0.0, 1.0, 0x0000ff],
				]
			ros_cloud = pc2.create_cloud(Header(frame_id="world"), FIELDS_XYZ , TEST_CLOUD_POINTS)

			# publish cloud
		pub.publish(ros_cloud)
		rospy.loginfo("Conversion and publish success ...\n")
		rospy.sleep(1)


received_ros_cloud_1 = None 
received_ros_cloud_2 = None 
received_open3d_cloud_1 = None
received_open3d_cloud_2 = None

def draw_registration_result(source, target, transformation_1, transformation_2):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation_1)
    target_temp.transform(transformation_2)
    
    pcd_combined = source_temp + target_temp
    open3d.visualization.draw_geometries([pcd_combined])
    print("Drawing registration result")
    publish_cloud(pcd_combined)

def transform_frames():
	print("In transform frame")
	listener = tf.TransformListener()
	rospy.sleep(2)
	trans1,quat1 =listener.lookupTransform("world","kinect_optical_frame",rospy.Time())
	trans2,quat2 = listener.lookupTransform("world","realSense_depth_optical_frame",rospy.Time())

	htm1 = tf.transformations.quaternion_matrix(quat1)
	htm2 = tf.transformations.quaternion_matrix(quat2)

	for i in range(0,3):
	
		htm1[i][3] = trans1[i]
		htm2[i][3] = trans2[i]

	return htm1, htm2


def callback(ros_cloud1, ros_cloud2):
	print("Inside callback")
	global received_ros_cloud_1
	global received_ros_cloud_2
	global received_open3d_cloud_1
	global received_open3d_cloud_2
	received_ros_cloud_1=ros_cloud1
	received_ros_cloud_2=ros_cloud2
	rospy.loginfo("-- Received ROS PointCloud2 message.")
	received_open3d_cloud_1 = convertCloudFromRosToOpen3d(received_ros_cloud_1)
	received_open3d_cloud_2 = convertCloudFromRosToOpen3d(received_ros_cloud_2)
	threshold = 0.02
	#trans_init = np.asarray([[ 0.5399724,  0.4402427,  0.7173675, -1.755],[-0.4402427,  0.8741447, -0.2050789, 0.501],[-0.7173675, -0.2050789,  0.6658276, 0.817], [0, 0, 0, 1]])
	trans_init_1,trans_init_2 = transform_frames()
	draw_registration_result(received_open3d_cloud_1,received_open3d_cloud_2, trans_init_1, trans_init_2)
	rospy.sleep(2)


	
if __name__ == "__main__":
	print("In main")
	rospy.init_node('test_pc_conversion_between_Open3D_and_ROS', anonymous=True)
	sub1 = message_filters.Subscriber('/kinect/depth/points', PointCloud2)
	sub2 = message_filters.Subscriber('/realsense/depth/points', PointCloud2)
	cb = message_filters.ApproximateTimeSynchronizer([sub1,sub2], queue_size=5, slop=0.1)
	print("here")
	cb.registerCallback(callback)
	pub = rospy.Publisher("/registered/depth/points", PointCloud2, queue_size=1)
	rospy.sleep(1)
	rospy.spin()
