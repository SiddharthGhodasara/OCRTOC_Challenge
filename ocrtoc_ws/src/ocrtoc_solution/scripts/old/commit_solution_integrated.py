#! /usr/bin/env python

import actionlib
import rospy

import ocrtoc_task.msg
from control_msgs.msg import GripperCommandActionGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math
#Our Imported Libraries
import tf
import os
import cv2
import sys
import copy
import time
import rospy
import tf2_ros
import actionlib
import numpy as np
import moveit_msgs.msg
import message_filters
import moveit_commander
import tf2_geometry_msgs
import geometry_msgs.msg
from std_msgs.msg import String
import xml.etree.ElementTree as ET
from sensor_msgs import point_cloud2
from std_msgs.msg import Header, Int64
from sensor_msgs.msg import PointCloud2
from gazebo_msgs.msg import ContactsState
from visualization_msgs.msg import MarkerArray
from tf.transformations import quaternion_from_euler
from control_msgs.msg import GripperCommandActionGoal
from geometry_msgs.msg import Point, Pose, PointStamped
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal
from goto import with_goto

from PIL import Image as img
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel
import rospkg


#Initalising the moveit commander
moveit_commander.roscpp_initialize(sys.argv)

#Global Variables
scale = 1
robot = None
scene = None
group = None
group_1 = None
label_pub = None
tf_buffer = None
tf_listener = None
gripper_cmd_pub = None
display_trajectory_publisher = None

#Defining the bridge
bridge = CvBridge()
dictionary = {"masterchef_chef_can": [0.102529, 0.102377, 0.140177],
"potted_meat_can": [0.057684, 0.101515, 0.083543],
"pudding_box" : [0.089631, 0.113077, 0.038256],
"wood_block": [0.206002, 0.089939, 0.090569],"jenga": [0.150000, 0.050000, 0.030000]}

#Defining camera info global varibale
camera_info = None
cam_model = None

#Loading the labels
rospack = rospkg.RosPack()
package_path = rospack.get_path('ocrtoc_solution')
print("Global")
labelsPath = os.path.sep.join([package_path, 'scripts','yolo', 'yolo-coco', "obj.names"])
LABELS = open(labelsPath).read().strip().split("\n")

#Initialize a list of colors to represent each possible class label
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

#Derive the paths to the YOLO weights and model configuration

weightsPath = os.path.sep.join([package_path, 'scripts','yolo' , 'yolo-coco', "yolov3-tiny-obj_5000.weights"])
configPath = os.path.sep.join([package_path, 'scripts','yolo', 'yolo-coco', "yolov3-tiny-obj.cfg"])

# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

#Contact Sensors Callback
contact1 = None
contact2 = None
def callback(msg1,msg2):
	global contact1
	global contact2
	contact1= msg1.states
	contact2= msg2.states

#Callback function for getting grasp coordinates
grasps_plots = ""
def callback_plots(msg_plots):
	global grasps_plots
	grasps_plots = msg_plots.data.split(" ")
	print(grasps_plots)

#Function to extract grasp coordinates
def get_grasps_coord():
	grasp_buffer = []
	#Subscribing to the topic publishing the coordinates of grasp
	grasps_plots_sub = rospy.Subscriber('/haf_grasping/grasp_hypothesis_with_eval', String, callback_plots)
	global grasps_plots
	# Wait for gsps to arrive.
	rate = rospy.Rate(1)

	#Running till we get a suitable grasp
	while not rospy.is_shutdown():
		if (grasps_plots != "" and grasps_plots[0] > 10):

			if int(grasps_plots[0]) < 70: #without scaling search area, the threshold was 70
				print("searching again for better grasp")
				grasp_buffer.append(grasps_plots)
				print(len(grasp_buffer))
				if len(grasp_buffer) >= 10:
					grasps_plots = max(grasp_buffer)
					print("The chosen grasp is: ")
					print(grasps_plots)
					break
				else:
					pass
			else:
				print("satisfied grasp condition")
				print(grasps_plots)
				break
		rate.sleep()


#Function for getting images from kinect camera
def get_image():
	image = rospy.wait_for_message('/kinect/color/image_raw', Image)
	#Try Except for exception handling
	try:
		#Converting Sensor Image to cv2 Image
		cv_img = bridge.imgmsg_to_cv2(image, 'bgr8')
		return cv_img

	except CvBridgeError as e:
		print(e)

#Function for converting coordinates to base link frame
def uv_to_xyz(cx, cy):
    #Converting to XYZ coordinates
    (x, y, z) = cam_model.projectPixelTo3dRay((cx, cy))
    #Normalising
    x = x/z
    y = y/z
    z = z/z

    #Getting the depth at given coordinates
    depth = rospy.wait_for_message('/kinect/depth/image_raw', Image)
    depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
    lookup = depth_img.load()
    d = lookup[cx, cy]

    #Modifying the coordinates
    x *= d
    y *= d
    z *= d

    #Making Point Stamp Message
    grasp_pose = geometry_msgs.msg.PointStamped()
    grasp_pose.header.frame_id = "/kinect_optical_frame"
    point = geometry_msgs.msg.Point()
    grasp_pose.point.x =  x
    grasp_pose.point.y =  y
    grasp_pose.point.z =  z

    #Transforming
    target_frame = "world"
    source_frame = "kinect_optical_frame"
    transform = tf_buffer.lookup_transform(target_frame, source_frame, rospy.Time(0), rospy.Duration(1.0))
    pose_transformed = tf2_geometry_msgs.do_transform_point(grasp_pose, transform)

    #Returning the transform coordinates
    return pose_transformed


#Function for YOLO Object Detection
def yolo(ll, scale):
	#Getting the image
	image = get_image()
	print("Got label {}".format(ll))

	#Getting the image dimensions
	(H, W) = image.shape[:2]
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
		for i in idxs.flatten():
			#Extracting the bounding box coordinates
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			#Getting the labels
			label = LABELS[classIDs[i]]
			print(label)
			if label == ll:
				#Getting center coordinates
				cx = x + (w/2)
				cy = y + (h/2)

				#Getting the width and height of the object and multipling it by scaling factor
				if label in dictionary.keys():
					h = dictionary[label][0] * scale
					w = dictionary[label][1] * scale

				#Converting the center cooridnates to base link frame
				xy_pose = uv_to_xyz(cx, cy)
				#Converting the extreme cooridnates to base link frame
				xy_pose_2 = uv_to_xyz(x, y)
				#Publishing the pose
				xy_pose.header.frame_id = label + " ,"  + str(w) + " ," + str(h)
				while pub.get_num_connections() < 1:
					None
				pub.publish(xy_pose)
				print("Published")
				return xy_pose

#Solution Class
class CommitSolution(object):
	def __init__(self, name):
		# Init action.
		self.action_name = name
		self.action_server = actionlib.SimpleActionServer(
			self.action_name, ocrtoc_task.msg.CleanAction,
			execute_cb=self.execute_callback, auto_start=False)
		self.action_server.start()
		rospy.loginfo(self.action_name + " is running.")

		self.arm_cmd_pub = rospy.Publisher(
			rospy.resolve_name('arm_controller/command'),
			JointTrajectory, queue_size=10)
		self.gripper_cmd_pub = rospy.Publisher(
			rospy.resolve_name('gripper_controller/gripper_cmd/goal'),
			GripperCommandActionGoal, queue_size=10)

		# create messages that are used to publish feedback/result.
		self.feedback = ocrtoc_task.msg.CleanFeedback()
		self.result = ocrtoc_task.msg.CleanResult()

		# get models directory.
		materials_path = rospy.get_param('~materials_dir','/root/ocrtoc_materials')
		self.models_dir = materials_path + '/models'
		rospy.loginfo("Models dir: " + self.models_dir)

	#Function to reaarange the goal list, if the robot has picked wrong object
	def rearrange(self, i, label, goal):
		#Getting the index of the currently picked object
		idx = goal.object_list.index(label)

		#Checking if it doesnt picks pervious objects
		if idx > i:
			#Replacing the pervoius object with current object in goal list
			goal.object_list[i], goal.object_list[idx] = goal.object_list[idx],goal.object_list[i]
			goal.scale_list[i], goal.scale_list[idx] = goal.scale_list[idx], goal.scale_list[i]
			goal.pose_list[i].position.x , goal.pose_list[idx].position.x = goal.pose_list[idx].position.x , goal.pose_list[i].position.x
			goal.pose_list[i].position.y, goal.pose_list[idx].position.y = goal.pose_list[idx].position.y, goal.pose_list[i].position.y
			goal.pose_list[i].position.z, goal.pose_list[idx].position.z = goal.pose_list[idx].position.z, goal.pose_list[i].position.z
		return goal

	#@with_goto
	def execute_callback(self, goal):
		#Defining the use of global variables
		global robot
		global scene
		global group
		global group_1
		global label_pub
		global tf_buffer
		global tf_listener
		global gripper_cmd_pub
		global display_trajectory_publisher

		rospy.loginfo("Get clean task.")
		print(goal)
		##### User code example starts #####
		# In the following, an example is provided on how to use the predefined software APIs
		# to get the target configuration, to control the robot, to set the actionlib result.

		#Looping over the list of objects
		for i in range(len(goal.object_list)):
			#Extracting the name of the object
			name = goal.object_list[i]
			global label_pub
			rospy.loginfo(type(name))
			#while label_pub.get_num_connections() < 1:
			#	None
			#label_pub.publish(str(name) + ",1," + str(goal.scale_list[i]))
			xy_pose = yolo(str(name), float(goal.scale_list[i]))
			rospy.Rate(1).sleep()

			#Getting the grasp coordinates
			new_grasps = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
			get_grasps_coord()
			global grasps_plots

			#print("THISSSSSSSSSSSSSSSSS is printinign ", int(grasps_plots[0]))
			if int(grasps_plots[0]) <= 55:
				print("Slide")

				#List to store the variables

				#Get coordinates of all the objects
				for i in range(len(goal.object_list)):
					obj_name = goal.object_list[i]
					#rospy.loginfo(type(name))
					#Getting YOLO coordinates
					xy_pose = yolo(str(name), float(goal.scale_list[i]))
					print(name, " ", xy_pose)

				#Find the distance vector between all the objects

				#Get the direction of movement

				#Slide


			#Extracting the X Y Z coordintes
			position_x = float(grasps_plots[-4])
			position_y = float(grasps_plots[-3])
			position_z = float(grasps_plots[-2])

			#Extracting the roll
			roll = float(grasps_plots[-1])
			print(grasps_plots[-1])
			print(roll)
			r,p,y= (roll - 90 ,90,0)

			#Generating a pose stamped messgae
			grasp_pose = geometry_msgs.msg.PoseStamped()
			grasp_pose.header.frame_id = "/world"
			#Assiging Linear Coordinates
			grasp_pose.pose.position.x = position_x
			grasp_pose.pose.position.y = position_y
			grasp_pose.pose.position.z = position_z + 0.05
			#Converting degrees to radians
			r_rad = (r*3.14159265358979323846)/180
			p_rad = (p*3.14159265358979323846)/180
			y_rad = (y*3.14159265358979323846)/180
			#Getting the Quaternion coordinates from Euler
			q = quaternion_from_euler(r_rad,p_rad,y_rad)
			print "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])
			#Assigning orientation value to pose message
			grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
			grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
			grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
			grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

			#Moving the arm to Picking location
			group.set_planning_time(50)
			group.set_pose_target(grasp_pose)
			plan2 = group.plan()
			group.go(wait=True)
			rospy.sleep(2)

			#Opening the gripper
			gripper_cmd = GripperCommandActionGoal()
			gripper_cmd.goal.command.position = 0.04
			gripper_cmd.goal.command.max_effort = 0.0
			gripper_cmd_pub.publish(gripper_cmd)
			rospy.loginfo("Pub gripper_cmd")
			rospy.sleep(2)

			#Going down to pick the object
			waypoints = []
			wpose = group.get_current_pose().pose
			wpose.position.z -= scale * 0.060
			waypoints.append(copy.deepcopy(wpose))
			(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
			group.execute(cartesian_plan, wait=True)
			rospy.sleep(2)

			#Closing the gripper till both contact sensors are touching the obejct
			rate = rospy.Rate(20)
			cmd = 0.039
			global contact
			while not rospy.is_shutdown():
				#Checking if both grippers are touching
				if len(contact1)>0 and len(contact2)>0:
				   print("contact")
				   break
				 #Checking if we are not reached the lower closinhg limit
				if cmd > 0.005:
					gripper_cmd.goal.command.position = cmd
					gripper_cmd.goal.command.max_effort = 0.01
					gripper_cmd_pub.publish(gripper_cmd)
					print(cmd)
					cmd -= 0.0005
					rate.sleep()
				#Re do the task if the lower limit is reached
				else:
					i = i - 1
					#goto .xxx
					break

			#Going down to pick the object
			waypoints = []
			wpose = group.get_current_pose().pose
			wpose.position.z += scale * 0.1
			waypoints.append(copy.deepcopy(wpose))
			(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
			group.execute(cartesian_plan, wait=True)

			#Check object
			rospy.loginfo(type(name))
			'''
			while label_pub.get_num_connections() < 1:
				None

			label_pub.publish(str(name) + ",2" + str(goal.scale_list[i][0]))
			'''
			#Getting YOLO's output
			# point_feedback = rospy.wait_for_message('/pose', PointStamped)
			# label_feedback = 'wood_block'
			# label_feedback = point_feedback.header.frame_id.split(',')[0]

			#Validating
			'''
			if name != label_feedback:
				goal = self.rearrange(i, label_feedback, goal)
				print(goal)
				print("label not matching")
'''
			#Getting the output location
			quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
			(r,p,y) = tf.transformations.euler_from_quaternion(quat, axes='sxyz')

			r,p,y= (r,1.57079632,0)

			#Getting the Quaternion coordinates from Euler
			q = quaternion_from_euler(r,p,y)
			print("Printing roll in degrees")
			print(math.degrees(r))
			grasp_pose.pose.position.x = goal.pose_list[i].position.x# + diff_x
			grasp_pose.pose.position.y = goal.pose_list[i].position.y# + diff_y
			grasp_pose.pose.position.z = position_z + 0.1
			grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
			grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
			grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
			grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

			#Moving the placing location, but 10cm above it
			group.set_planning_time(50)
			group.set_pose_target(grasp_pose)
			plan2 = group.plan()
			group.go(wait=True)
			rospy.sleep(1)

			#Going down to place the object
			waypoints = []
			wpose = group.get_current_pose().pose
			wpose.position.z -= goal.pose_list[i].position.z * 2
			waypoints.append(copy.deepcopy(wpose))
			(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
			group.execute(cartesian_plan, wait=True)
			rospy.sleep(1)

			#Opening the gripper
			group_1.set_named_target("gripper_open")
			plan3 = group_1.go(wait=True)

			#Moving up from the placing location
			waypoints = []
			wpose = group.get_current_pose().pose
			wpose.position.z += position_z + 0.1
			waypoints.append(copy.deepcopy(wpose))
			(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
			group.execute(cartesian_plan, wait=True)
			rospy.sleep(1)
			#	.xxx
			#Closing the gripper back
			group_1.set_named_target("gripper_close")
			plan3 = group_1.go(wait=True)

			#Going back to task pose
			group.set_named_target("pose1")
			plan3 = group.go(wait=True)
			rospy.sleep(10)

#Main Thread
if __name__ == '__main__':
	#Initializing the node
	rospy.init_node('commit_solution')

	#Defining the use of global variables
	global robot
	global scene
	global group
	global group_1
	global label_pub
	global tf_buffer
	global tf_listener
	global gripper_cmd_pub
	global display_trajectory_publisher

	#Initialising publishers, moveit controllers and other required things
	tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
	tf_listener = tf2_ros.TransformListener(tf_buffer)
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group = moveit_commander.MoveGroupCommander("arm_controller")
	group_1 = moveit_commander.MoveGroupCommander("gripper_controller")
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
	#Label Publisher
	label_pub = rospy.Publisher('/label', String, queue_size=1)
	#Defining the publisher
	global pub
	pub = rospy.Publisher('/pose', geometry_msgs.msg.PointStamped, queue_size = 10)
	#Gripper command publisher
	gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)
	#Contact Sensors Subscribers
	sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
	sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
	cb = message_filters.TimeSynchronizer([sub1, sub2], 10)
	cb.registerCallback(callback)

	#Getting camera info
	print("Running")
	camera_info = rospy.wait_for_message('/kinect/color/camera_info', CameraInfo)
	print("GOt Cam")
	#Making Camera Model
	global cam_model
	cam_model = PinholeCameraModel()
	cam_model.fromCameraInfo(camera_info)

	#Going the task pose
	group.set_named_target("pose1")
	plan = group.go(wait=True)

	commit_solution = CommitSolution('commit_solution')
	print("Here")
	rospy.spin()
