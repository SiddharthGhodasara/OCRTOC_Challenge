#! /usr/bin/env python
import tf
import os
import cv2
import sys
import math
import rospy
import rospkg
import tf2_ros
import numpy as np
import open3d as o3d
import tf2_geometry_msgs
from PIL import Image as img
from image_geometry import PinholeCameraModel
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import PoseStamped, PointStamped
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
from tf.transformations import quaternion_from_euler, euler_from_quaternion

#Defining the class
class Perception:
#/home/gaurav/ocrtoc_ws/src/3D_Pose_Estimation/yolo_less_objs/yolov3-tiny-obj_best.weights
    #Init function
	def __init__(self, image_topic = "/kinect/color/image_raw", depth_topic = "/kinect/depth/image_raw", camera_frame = "kinect_optical_frame",	camera_topic = '/kinect/color/camera_info'):
		self.image = None
		#Loading the labels
		rospack = rospkg.RosPack()
		package_path = rospack.get_path('3D_Pose_Estimation')
		labelsPath = os.path.sep.join([package_path, 'yolo_less_objs', 'obj.names'])
		self.pcd_path = os.path.sep.join([package_path, 'meshes'])
		self.LABELS = open(labelsPath).read().strip().split("\n")

		#Derive the paths to the YOLO weights and model configuration
		weightsPath = os.path.sep.join([package_path, 'yolo_less_objs', "yolov3-tiny-obj_5000.weights"])#yolov3-tiny-obj_best.weights"])
		configPath = os.path.sep.join([package_path, 'yolo_less_objs', "yolov3-tiny-obj.cfg"])

		# Load our YOLO object detector trained on custom data
		print("[INFO] loading YOLO from disk...")
		self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

		# Loading all the meshes
		self.meshes_dir = {}
		print("[INFO] loading Meshes from disk...")
		for fil in os.listdir(self.pcd_path):
			obj_mesh_path = os.path.sep.join([self.pcd_path, fil])
			obj_label = fil.split('/')[-1].split('.')[0]
			self.meshes_dir[obj_label] = o3d.io.read_point_cloud(obj_mesh_path)

		#Defining Voxel Size
		self.voxel_size = 0.005 #mm

		# Tranform Listener
		self.tf_listener = None
		# Transformations
		self.tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))

		self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

		#Defining the topics
		self.image_topic = image_topic
		self.depth_topic = depth_topic
		self.camera_frame = camera_frame
		self.camera_topic = camera_topic

		#Defining the subscriber
		rospy.Subscriber(self.image_topic, Image, self.image_cb)

		#Defining the bridge
		self.bridge = CvBridge()

		#Getting the camera info
		self.camera_info = rospy.wait_for_message(self.camera_topic, CameraInfo)
		#Making Camera Model
		self.cam_model = PinholeCameraModel()
		self.cam_model.fromCameraInfo(self.camera_info)


	#Image Callback Function
	def image_cb(self, image):
		try:
			#Converting Sensor Image to cv2 Image
			self.image = self.bridge.imgmsg_to_cv2(image, 'bgr8')
		
		#Handling exceptions
		except CvBridgeError as e:
			print(e)


	#Function for converting coordinates to base link frame
	def uv_to_xyz(self, cx, cy):
		#Converting to XYZ coordinates
		(x, y, z) = self.cam_model.projectPixelTo3dRay((cx, cy))
		#Normalising
		x, y, z = x/z, y/z, z/z

		#Getting the depth at given coordinates
		depth = rospy.wait_for_message(self.depth_topic, Image)
		depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
		lookup = depth_img.load()
		d = lookup[cx, cy]

		#Modifying the coordinates
		x, y, z = x*d, y*d, z*d

		#Making Point Stamp Message
		point_wrt_camera = PointStamped()
		point_wrt_camera.header.frame_id = self.camera_frame
		point_wrt_camera.point.x =  x
		point_wrt_camera.point.y =  y
		point_wrt_camera.point.z =  z

		#Transforming
		target_frame = "world"
		source_frame = self.camera_frame
		transform = self.tf_buffer.lookup_transform(target_frame,
											source_frame, #source frame
											rospy.Time(0), #get the tf at first available time
											rospy.Duration(1.0)) #wait for 1 second

		self.point_wrt_world = tf2_geometry_msgs.do_transform_point(point_wrt_camera, transform)
		
	
	#Function to get bounding box dimensions of req_object
	def get_dim(self, req_label):
		#Getting the 3D bounding box of the mesh to extract the size
		bounding_box = self.meshes_dir[req_label].get_axis_aligned_bounding_box()
		points = bounding_box.get_box_points()

		points_array = np.asarray(points)

		length = ((points_array[0][0] - points_array[1][0])**2 + (points_array[0][1] - points_array[1][1])**2 + (points_array[0][2] - points_array[1][2])**2)**0.5
		width = ((points_array[0][0] - points_array[2][0])**2 + (points_array[0][1] - points_array[2][1])**2 + (points_array[0][2] - points_array[2][2])**2)**0.5
		height = ((points_array[0][0] - points_array[3][0])**2 + (points_array[0][1] - points_array[3][1])**2 + (points_array[0][2] - points_array[3][2])**2)**0.5

		return length, width, height


	#Function to find transform between camera_frame and world
	def transform_frames(self):
		#Finding the transform
		trans1, quat1 = self.tf_listener.lookupTransform("world", self.camera_frame, rospy.Time())

		htm1 = tf.transformations.quaternion_matrix(quat1)

		for i in range(0,3):
			htm1[i][3] = trans1[i]

		return htm1


	#Function to preprocess point cloud before registration
	def preprocess_point_cloud(self, pcd):
		print(":: Downsample with a voxel size %.3f." % self.voxel_size)
		pcd_down = pcd.voxel_down_sample(self.voxel_size)

		radius_normal = self.voxel_size * 2
		print(":: Estimate normal with search radius %.3f." % radius_normal)
		pcd_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

		radius_feature = self.voxel_size * 5
		print(":: Compute FPFH feature with search radius %.3f." % radius_feature)
		pcd_fpfh = o3d.registration.compute_fpfh_feature(pcd_down, o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
		return pcd_down, pcd_fpfh


	#Function to preprocess both the point clouds and transform them as required
	def prepare_dataset(self, source, target, transform):
		print(":: Load two point clouds and disturb initial pose.")
						
		#source.transform(transform)
		target.transform(transform)

		#draw_registration_result(source, target, np.identity(4))

		source_down, source_fpfh = self.preprocess_point_cloud(source, self.voxel_size)
		target_down, target_fpfh = self.preprocess_point_cloud(target, self.voxel_size)
		return source, tasrget, source_down, target_down, source_fpfh, target_fpfh


	#Function to register point cloud using FPFH features
	def execute_global_registration(self, source_down, target_down, source_fpfh,
									target_fpfh):
		distance_threshold = self.voxel_size * 1.5
		print(":: RANSAC registration on downsampled point clouds.")
		print("   Since the downsampling voxel size is %.3f," % self.voxel_size)
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


	#Function to refine registratiin using ICP registration
	def refine_registration(self, source, target, source_fpfh, target_fpfh, transformation):
		distance_threshold = self.voxel_size * 0.4
		print(":: Point-to-plane ICP registration is applied on original point")
		print("   clouds to refine the alignment. This time we use a strict")
		print("   distance threshold %.3f." % distance_threshold)
		result = o3d.registration.registration_icp(source, target, distance_threshold,transformation,
			o3d.registration.TransformationEstimationPointToPlane())
		return result

	
	#Function to get transforms as we need it
	def get_total_transformation_pose(self, rot_transform, trans_transform):
		trans = [trans_transform[0][3], trans_transform[1][3], trans_transform[2][3]]

		rot_mat = np.eye(4)
		rot_mat[:3,:3] = ((rot_transform[0][0], rot_transform[0][1], rot_transform[0][2]),(rot_transform[1][0], rot_transform[1][1], rot_transform[1][2]),(rot_transform[2][0], rot_transform[2][1], rot_transform[2][2]))

		rot = tf.transformations.quaternion_from_matrix(rot_mat)

		pose_6d = PoseStamped()
		pose_6d.header.frame_id = 'world'
		pose_6d.pose.position.x = trans[0]
		pose_6d.pose.position.y = trans[1]
		pose_6d.pose.position.z = trans[2]
		pose_6d.pose.orientation.x = rot[0]
		pose_6d.pose.orientation.y = rot[1]
		pose_6d.pose.orientation.z = rot[2]
		pose_6d.pose.orientation.w = rot[3]
		
		return pose_6d

	
	#Function to predict and return the pose message	
	def predict(self, req_label, req_type = '3D'):

		while(self.image is None): 
			rospy.sleep(1)
		#Getting the image dimensions
		(self.H, self.W) = self.image.shape[:2]

		self.center = (self.W/2, self.H/2)
		self.focal_length = self.center[0] / np.tan(60/2 * np.pi / 180)
		self.camera_matrix = np.array([[self.focal_length, 0, self.center[0]],
											[0, self.focal_length, self.center[1]],
											[0, 0, 1]], dtype = "double")

		# determine only the *output* layer names that we need from YOLO
		ln = self.net.getLayerNames()
		ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
		#Creating Blob from images
		blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
		
		#Feeding the blob as input
		self.net.setInput(blob)
		#Forward pass
		layerOutputs = self.net.forward(ln)

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
		            box = detection[0:4] * np.array([self.W, self.H, self.W, self.H])
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
			for i in idxs.flatten():
				#Extracting the bounding box coordinates
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])
				#Getting the labels
				label = self.LABELS[classIDs[i]]
				
				if req_label == label:
					#center coordinates
					cx = x + (w/2)
					cy = y + (h/2)

					#Converting the center cooridnates to base link frame
					self.uv_to_xyz(cx, cy)

					#Converitng PointStamped to PoseStamped
					self.pose_wrt_world = PoseStamped()
					self.pose_wrt_world.header.frame_id = 'world'
					self.pose_wrt_world.pose.position.x = self.point_wrt_world.point.x
					self.pose_wrt_world.pose.position.y = self.point_wrt_world.point.y
					self.pose_wrt_world.pose.position.z = self.point_wrt_world.point.z
					self.pose_wrt_world.pose.orientation.x = 0.0
					self.pose_wrt_world.pose.orientation.y = 0.707
					self.pose_wrt_world.pose.orientation.z = 0.0
					self.pose_wrt_world.pose.orientation.w = 0.707

					#Checking if we need 3D pose or 6D
					if req_type == '3D':
						return self.pose_wrt_world
					
					else:
						#Comupting Initial Transformation Matrix
						trans_init = np.array([[1.0, 0.0, 0.0, self.point_wrt_world.point.x], 
												[0.0, 1.0, 0.0, self.point_wrt_world.point.y], 
												[0.0, 0.0, 1.0, self.point_wrt_world.point.z], 
												[0.0, 0.0, 0.0, 1.0]])

						#Extracting the bounding box image
						box_img = self.image[y-10 : y+h+10, x-10 : x+w+10]
						
						#Converting to RGB Color Space
						box_img = cv2.cvtColor(box_img, cv2.COLOR_BGR2RGB)

						#Getting the depth image
						self.depth = rospy.wait_for_message(self.depth_topic, Image)
						
						try:
							#Converting to cv2 image from sensor_msg image
							self.depth_converted = self.bridge.imgmsg_to_cv2(self.depth, desired_encoding='passthrough')
						except CvBridgeError, e:
							print e

						#Converting to np array
						self.depth_array = np.array(self.depth_converted)

						#Extracting the depth image of the bounding box
						self.depth_box = self.depth_array[y-10 : y+h+10, x-10 : x+w+10]

						#Generating open3D RGBD Image
						self.o3d_rgbd = o3d.geometry.RGBDImage()
						o3d_rgbd_color = o3d.geometry.Image(self.box_img)
						o3d_rgbd_depth = o3d.geometry.Image(self.depth_box.astype(np.float32))
						self.o3d_rgbd.color = o3d_rgbd_color
						self.o3d_rgbd.depth = o3d_rgbd_depth
						
						#Computing Intrinsic Parameters of Camera
						intrinsic = o3d.camera.PinholeCameraIntrinsic()
						intrinsic.set_intrinsics(self.W, self.H, self.focal_length, self.focal_length, self.center[0], self.center[1])

						#Generating Point Cloud from RGBD Image
						self.rgbd_pointcloud = o3d.geometry.PointCloud.create_from_rgbd_image(self.o3d_rgbd, intrinsic)

						#Reading the source comprasion file
						self.mesh_pointcloud = self.meshes_dir[req_label]

						#Preprcoessing the point clouds
						source, target, source_down, target_down, source_fpfh, target_fpfh = self.prepare_dataset(self.mesh_pointcloud, self.rgbd_pointcloud, self.voxel_size, self.transform_frames())

						#Global Registration
						result_ransac = self.execute_global_registration(source_down, target_down,source_fpfh, target_fpfh)

						#Local Refinement
						result_icp = self.refine_registration(source_down, target_down, source_fpfh, target_fpfh, result_ransac.transformation)

						print(result_ransac.fitness, result_icp.inlier_rmse)
						
						self.pose_6d_wrt_world = self.get_total_transformation_pose(result_icp.transformation, trans_init)

						return self.pose_6d_wrt_world

			#Label not found
			return None
