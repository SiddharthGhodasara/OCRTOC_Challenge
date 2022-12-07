#!/usr/bin/env python

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

def preprocess_point_cloud(pcd):
	voxel_size = 0.5
	pcd_down = o3d.geometry.voxel_down_sample(pcd, voxel_size)
	
	pcd_fpfh = o3d.registration.compute_fpfh_feature(
        pcd_down,
        o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 5.0,
                                             max_nn=100))
	return (pcd_down, pcd_fpfh)

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])

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

def convertCloudFromOpen3dToRos(open3d_cloud, frame_id="base_link"):
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

def register_point_cloud_fpfh(source, target, source_fpfh, target_fpfh, config):
	distance_threshold = config["voxel_size"] * 1.4
	if config["global_registration"] == "fgr":
		result = o3d.registration.registration_fast_based_on_feature_matching(
			source, target, source_fpfh, target_fpfh,
			o3d.registration.FastGlobalRegistrationOption(
				maximum_correspondence_distance=distance_threshold))

	if config["global_registration"] == "ransac":
		result = o3d.registration.registration_ransac_based_on_feature_matching(
			source, target, source_fpfh, target_fpfh, distance_threshold,
			o3d.registration.TransformationEstimationPointToPoint(False), 4, [
				o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
				o3d.registration.CorrespondenceCheckerBasedOnDistance(
					distance_threshold)
			], o3d.registration.RANSACConvergenceCriteria(4000000, 500))

	if (result.transformation.trace() == 4.0):
		return (False, np.identity(4), np.zeros((6, 6)))

	information = o3d.registration.get_information_matrix_from_point_clouds(
		source, target, distance_threshold, result.transformation)

	if information[5, 5] / min(len(source.points), len(target.points)) < 0.3:
		return (False, np.identity(4), np.zeros((6, 6)))

	return (True, result.transformation, information)

if __name__ == "__main__":

	rospy.init_node('test_pc_conversion_between_Open3D_and_ROS', anonymous=True)
	received_ros_cloud = rospy.wait_for_message('/pcl/points', PointCloud2)
	print("Got point Cloud ")
	open3d_cloud = convertCloudFromRosToOpen3d(received_ros_cloud)

	#Getting features
	open3d_cloud_down, target_feature = preprocess_point_cloud(open3d_cloud)
	print("Length of target features: ", target_feature)
	
    #Reading the point cloud
	pcd = o3d.io.read_point_cloud("/home/kaushik/object1.pcd")

	input_down, source_feature = preprocess_point_cloud(pcd)
	print("Length of target features: ", source_feature)
	trans_init = np.asarray([[0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
	
	threshold = 0.02

	#config = {'voxel_size' : 0.5, 'global_registration': 'ransac'}

	#_, trans, info = register_point_cloud_fpfh(input_down, open3d_cloud_down, source_feature, target_feature, config)

	
	reg_p2p = o3d.registration.registration_icp(
        pcd, open3d_cloud, threshold, trans_init,
        o3d.registration.TransformationEstimationPointToPoint())
	print(reg_p2p.transformation)
	#print("Transformation is: ")
	#print(trans, _)
	


	#print("Information is:")
	#print(info)

	draw_registration_result(pcd, open3d_cloud, reg_p2p.transformation)

	#beta = -np.arcsin(reg_p2p[2,0])
