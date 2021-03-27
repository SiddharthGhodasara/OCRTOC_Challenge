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

	
if __name__ == "__main__":

	rospy.init_node('test_pc_conversion_between_Open3D_and_ROS', anonymous=True)
	received_ros_cloud = rospy.wait_for_message('/pcl/points', PointCloud2)
	print("Got point Cloud ")

	#Converitng PointCloud2 to Open3D point cloud
	open3d_cloud = convertCloudFromRosToOpen3d(received_ros_cloud)

	o3d.visualization.draw_geometries([open3d_cloud])

	#VoxelGrade Downsampling
	#downpcd = o3d.geometry.voxel_down_sample(open3d_cloud, voxel_size=0.05)

	#Saving the point cloud
	o3d.io.write_point_cloud("/home/kaushik/PCD/cordless_drill.pcd", open3d_cloud)
	print("Saved Point Cloud")
