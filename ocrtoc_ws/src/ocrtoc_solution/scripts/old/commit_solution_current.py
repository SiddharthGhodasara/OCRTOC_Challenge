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
from std_msgs.msg import *
from sensor_msgs.msg import PointCloud2
from gazebo_msgs.msg import ContactsState
from visualization_msgs.msg import MarkerArray
from tf.transformations import quaternion_from_euler
from control_msgs.msg import GripperCommandActionGoal
from geometry_msgs.msg import Point, Pose, PointStamped
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal
from PIL import Image as img
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel
import rospkg
from shapely.geometry import Polygon

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
swap_name = None
retry = 0

obj_size = {}
obj_pose = {}

#Defining camera info global varibale
camera_info = None
cam_model = None

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

#Function to extract grasp coordinates
def get_grasps_coord():
	grasp_buffer = []
	#Subscribing to the topic publishing the coordinates of grasp
	grasps_plots_sub = rospy.Subscriber('/haf_grasping/grasp_hypothesis_with_eval', String, callback_plots)
	global grasps_plots
	# Wait for gsps to arrive.
	rate = rospy.Rate(2)

	#Running till we get a suitable grasp
	while not rospy.is_shutdown():

		if (grasps_plots != "" and grasps_plots[0] > 2):

			if int(grasps_plots[0]) < 100: #without scaling search area, the threshold was 70
				
				grasp_buffer.append(grasps_plots)
				
				if len(grasp_buffer) >= 2: 
					last_ten = grasp_buffer[-2:-1]
					grasps_plots = max(last_ten)

					break
				else:
					pass
			else:
				print("satisfied grasp condition")
				
				break
		rate.sleep()

image = None 


def yolo_cb(data):
	global obj_pose
	global obj_size

	pose = data
	header = pose.header.frame_id
	header_list = header.split(',')
	label = str(header_list[0])
	obj_len = float(header_list[1])
	obj_width = float(header_list[2])
	obj_height = float(header_list[3])

	if label not in obj_size.keys():
		obj_size[label] = [obj_len, obj_width, obj_height]

	obj_pose[label] = pose 

#Function for YOLO Object Detection
def yolo(required_label):

	if required_label not in obj_pose.keys():
		return None
	else:
		return obj_pose[required_label]

	
def do_task(goal, i):

	tc = i
	#while(tc<len(goal.object_list)):
	name = str(goal.object_list[tc])
	curr_x = goal.pose_list[tc].position.x
	curr_y = goal.pose_list[tc].position.y

	while name not in obj_size.keys():
		rospy.sleep(1)

	curr_h = obj_size[name][0] * float(goal.scale_list[tc])
	curr_w = obj_size[name][1] * float(goal.scale_list[tc])

	curr_x1, curr_y1 = curr_x - curr_w/2, curr_y - curr_h/2
	curr_x2, curr_y2 = curr_x - curr_w/2, curr_y + curr_h/2
	curr_x3, curr_y3 = curr_x + curr_w/2, curr_y - curr_h/2
	curr_x4, curr_y4 = curr_x + curr_w/2, curr_y + curr_h/2

	box_1 = [[curr_x1, curr_y1], [curr_x2, curr_y2], [curr_x4, curr_y4], [curr_x3, curr_y3]]

	poly_1 = Polygon(box_1)

	#Get the cuurent coordinates of all other objects
	for j in range(0, len(goal.object_list)):
		if j == tc: 
			continue
	
		pose = yolo(str(goal.object_list[j]))
		
		if (pose == None):
			j+=1
			continue
		#Define the region of cuurent yolo object
		var_list = pose.header.frame_id.split(",")
		label = var_list[0]

		#Length of object
		w = obj_size[label][0]
		#Width of object
		h = obj_size[label][0]

		x = pose.pose.position.x
		y = pose.pose.position.y

		x1, y1 = x - w/2, y - h/2
		x2, y2 = x - w/2, y + h/2
		x3, y3 = x + w/2, y - h/2
		x4, y4 = x + w/2, y + h/2
		box_2 = [[x1, y1], [x2, y2], [x4, y4], [x3, y3]]
		poly_2 = Polygon(box_2)
		
		swap = 0
			#Check for intersection
		if poly_1.intersection(poly_2).area != 0:
			global swap_name 
			if swap_name == goal.object_list[tc]:
				swap = 1
				break
			else:
				
				swap_name = goal.object_list[j]
				goal.object_list[tc], goal.object_list[j] = goal.object_list[j],goal.object_list[tc]
				goal.pose_list[tc].position.x , goal.pose_list[j].position.x = goal.pose_list[j].position.x , goal.pose_list[tc].position.x
				goal.pose_list[tc].position.y, goal.pose_list[j].position.y = goal.pose_list[j].position.y, goal.pose_list[tc].position.y
				goal.pose_list[tc].position.z, goal.pose_list[j].position.z = goal.pose_list[j].position.z, goal.pose_list[tc].position.z
					
				goal.pose_list[tc].orientation.x , goal.pose_list[j].orientation.x  =goal.pose_list[j].orientation.x , goal.pose_list[tc].orientation.x 
				goal.pose_list[tc].orientation.y , goal.pose_list[j].orientation.y  =goal.pose_list[j].orientation.y , goal.pose_list[tc].orientation.y
				goal.pose_list[tc].orientation.z , goal.pose_list[j].orientation.z  =goal.pose_list[j].orientation.z , goal.pose_list[tc].orientation.z
				goal.pose_list[tc].orientation.w , goal.pose_list[j].orientation.w  =goal.pose_list[j].orientation.w , goal.pose_list[tc].orientation.w
				return goal,i

	#Failure resistance if object is not resistant 	
	name = goal.object_list[i]
	global label_pub
	rospy.loginfo(type(name))
	xy_pose = yolo(str(name))
	if (xy_pose == None):
		i+=1
		print("Object not detected by YOLO, skipping", name)
		return goal, i

	# rospy.Rate(1).sleep()
	rs_state = 0
	#Extracting centroid coordiantes from YOLO
	yolo_x = xy_pose.pose.position.x
	yolo_y = xy_pose.pose.position.y
	yolo_z = xy_pose.pose.position.z

	print(yolo_x, yolo_y, yolo_z)
	#Generating a pose stamped messgae
	rs_pose = geometry_msgs.msg.PoseStamped()
	rs_pose.header.frame_id = "/world"
	#Assiging Linear Coordinates
	rs_pose.pose.position.x = yolo_x - 0.06
	rs_pose.pose.position.y = yolo_y 
	rs_pose.pose.position.z = yolo_z + 0.17
	#Converting degrees to radians
	r_rad_rs = 0
	p_rad_rs = math.pi/2
	y_rad_rs = 0
	#Getting the Quaternion coordinates from Euler
	q_rs = quaternion_from_euler(r_rad_rs,p_rad_rs,y_rad_rs)
		
	#Assigning orientation value to pose message
	rs_pose.pose.orientation.x = q_rs[0]#quat[0] #grasps_plots.orientation.x
	rs_pose.pose.orientation.y = q_rs[1]#quat[1] #grasps_plots.orientation.y
	rs_pose.pose.orientation.z = q_rs[2]#quat[2] #grasps_plots.orientation.z
	rs_pose.pose.orientation.w = q_rs[3]#quat[3] #grasps_plots.orientation.w

	#Moving the arm to Picking location
	group.set_planning_time(50)
	group.set_pose_target(rs_pose)
	plan2 = group.plan()
	rs_state = group.go(wait=True)
	rospy.sleep(1)
	print("before publishing control message to haf grasping")
	#Sending control message to haf_grasping 
	if (rs_state):
		rs_state_pub.publish(1.0)
		print("published control message to haf grasping")

	#Getting the grasp coordinates
	new_grasps = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
	get_grasps_coord()
	global grasps_plots
	print(new_grasps)
	#Extracting the X Y Z coordintes
	position_x = float(grasps_plots[-4])
	position_y = float(grasps_plots[-3])
	position_z = float(grasps_plots[-2])

	#Calculating difference between centroid and grasping center
	diff_x = yolo_x - position_x
	diff_y = yolo_y - position_y

	#Extracting the roll
	roll = float(grasps_plots[-1])
	print(grasps_plots[-1])
	print(roll)
	r,p,y= (roll + 90 ,90,0)

	#Generating a pose stamped messgae
	grasp_pose = geometry_msgs.msg.PoseStamped()
	grasp_pose.header.frame_id = "/world"
	#Assiging Linear Coordinates
	grasp_pose.pose.position.x = position_x
	grasp_pose.pose.position.y = position_y
	grasp_pose.pose.position.z = position_z + 0.03
	#Converting degrees to radians
	r_rad = (r*3.14159265358979323846)/180
	p_rad = (p*3.14159265358979323846)/180
	y_rad = (y*3.14159265358979323846)/180
	#Getting the Quaternion coordinates from Euler
	q = quaternion_from_euler(r_rad,p_rad,y_rad)
	
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
	rospy.sleep(1)

	#Opening the gripper
	gripper_cmd = GripperCommandActionGoal()
	gripper_cmd.goal.command.position = 0.04
	gripper_cmd.goal.command.max_effort = 0.0
	gripper_cmd_pub.publish(gripper_cmd)
	rospy.loginfo("Pub gripper_cmd")
	rospy.sleep(1)

	#Going down to pick the object
	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z -= scale * 0.030 + 0.015
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)
	rospy.sleep(1)

	#Closing the gripper till both contact sensors are touching the obejct
	rate = rospy.Rate(20)
	cmd = 0.039
	closure = -1
	global retry 

	#Failure case: The robot doesn't grasp object - go back to task pose to save time 
	global contact
	while not rospy.is_shutdown():
		#Checking if both grippers are touching
		if len(contact1)>0 and len(contact2)>0:
			closure = 1
			retry = 0
			break


		 #Checking if we are not reached the lower closinhg limit
		if cmd > 0.005:
			gripper_cmd.goal.command.position = cmd
			gripper_cmd.goal.command.max_effort = 0.01
			gripper_cmd_pub.publish(gripper_cmd)
			cmd -= 0.0005
			rate.sleep()

		#Re do the task if the lower limit is reached
		else:
			closure = 0
			break

	if (closure == 0 and retry < 3): 

		print("Missed object, going back to pose1 and trying again")
		#Opening the gripper
		group_1.set_named_target("gripper_open")
		plan3 = group_1.go(wait=True)

		#Moving up from the placing location
		waypoints = []
		wpose = group.get_current_pose().pose
		wpose.position.z += position_z + 0.15
		waypoints.append(copy.deepcopy(wpose))
		(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
		group.execute(cartesian_plan, wait=True)
		rospy.sleep(1)

		#Closing the gripper back
		group_1.set_named_target("gripper_close")
		plan3 = group_1.go(wait=True)

		#Going back to pose1
		group.set_named_target("pose1")
		plan3 = group.go(wait=True)
		retry+=1
		return goal, i

	#Going down to pick the object
	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z += scale * 0.15
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)

	#Check object
	rospy.loginfo(type(name))
	
	#Getting the output location
	quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
	(r,p,y) = tf.transformations.euler_from_quaternion(quat, axes='sxyz')

	r,p,y= (r ,1.57079632,0)

	if name == "pudding_box" or name == "potted_meat_can" or swap == 1:
		r = r + 1.57079632

	#Getting the Quaternion coordinates from Euler
	q = quaternion_from_euler(r,p,y)
	grasp_pose.header.frame_id = "/world"
	grasp_pose.pose.position.x = goal.pose_list[i].position.x - diff_x
	grasp_pose.pose.position.y = goal.pose_list[i].position.y + diff_y
	grasp_pose.pose.position.z = position_z + 0.1
	grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
	grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
	grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
	grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

	if swap == 1: 
		grasp_pose.pose.position.x = 0.3126
		grasp_pose.pose.position.y = 0

	#Moving the placing location, but 10cm above it
	group.set_planning_time(50)
	group.set_pose_target(grasp_pose)
	plan2 = group.plan()
	
	ret_group_go = group.go(wait=True)
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

	#Closing the gripper back
	group_1.set_named_target("gripper_close")
	plan3 = group_1.go(wait=True)
	
	#Going back to task pose
	group.set_named_target("pose1")
	plan3 = group.go(wait=True)
	rospy.sleep(2)

	if swap != 1: 
		res_im_feedback = feedback_immediate(goal,i)
		counter = 0
		while (int(res_im_feedback)!=1 and counter < 2):
			res_im_feedback = feedback_immediate(goal,i)
			counter+=1
	i+=1
	
	return goal, i

#Feedback Function
def feedback(goal):
	#Looping over all the objects

	for i in range(len(goal.object_list)):
		#Getting the object label
		name = goal.object_list[i]
		#Sending to YOLO and getting output coordinates
		pose = yolo(str(name))
		if (pose == None):
			print("Object not detected by YOLO, skipping", name)
			i+=1
			continue
		#Extracting pose of current object
		pose_curr_x = pose.pose.position.x
		pose_curr_y = pose.pose.position.y
		
		#Checking if threshold is within threshold
		if abs(pose_curr_x - goal.pose_list[i].position.x) <= 0.03 and abs(pose_curr_y - goal.pose_list[i].position.y) <= 0.03:
			
			print("Good Job Translation for {}".format(name))
			if abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x) <= 0.15 and abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y) <= 0.15 and abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z) <= 0.15 and abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w) <= 0.15:
				print("Good Orientation")
			else:
				print("Error in x", abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x))
				print("Error in y", abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y))
				print("Error in z", abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z))
				print("Error in w", abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w))

		#If not within the threshold, do that object again
		else:
			print("Bad Job Translation for {}".format(name))
			goal, i = do_task(goal, i)

		#rospy.sleep(1)

def feedback_immediate(goal, i): 

	print("Evaluating feedback immediately")

	name = goal.object_list[i]
	#Sending to YOLO and getting output coordinates
	pose = yolo(str(name))
	if (pose == None):
		print("Object not detected by YOLO, skipping", name)
		i+=1
		return 1  
	#Extracting pose of current object
	pose_curr_x = pose.pose.position.x
	pose_curr_y = pose.pose.position.y

	(r1,p1,y1) = tf.transformations.euler_from_quaternion(pose.pose.orientation, axes='sxyz')
	(r2,p2,y2) = tf.transformations.euler_from_quaternion(goal.pose_list[i].orientation, axes='sxyz')
	print("Error in rpy: ")
	print((r2-r1), (p2-p1), (y2-y1))
	#Checking if threshold is within threshold
	if abs(pose_curr_x - goal.pose_list[i].position.x) <= 1 and abs(pose_curr_y - goal.pose_list[i].position.y) <= 1:

		print("Good Job Translation for {}".format(name))
		if abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x) <= 0.15 and abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y) <= 0.15 and abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z) <= 0.15 and abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w) <= 0.15:
			print("Good Orientation")
			print("Error in x", abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x))
			print("Error in y", abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y))
			print("Error in z", abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z))
			print("Error in w", abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w))
		else:
			print("Error in x", abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x))
			print("Error in y", abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y))
			print("Error in z", abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z))
			print("Error in w", abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w))
		return 1

	#If not within the threshold, do that object again
	else:

		print("Bad Job Translation for {}".format(name))
		goal, i = do_task(goal, i)
		return 0

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

	def execute_callback(self, goal):
		#Defining the use of global variables
		
		rospy.loginfo("Get clean task.")
		
		i = 0
		while(i<len(goal.object_list)):
			goal, i = do_task(goal, i)
			rospy.sleep(5)


		print("Going for 1st feedback")
		feedback(goal)
		print("Going for final feedback")
		feedback(goal)
		print("Done with feedback")

		self.result.status = "Finished"
		rospy.loginfo("Done.")
		self.action_server.set_succeeded(self.result)

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
	rs_state_pub = rospy.Publisher('/realsense_state', Float32, queue_size=10)
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
	#Label Publisher
	label_pub = rospy.Publisher('/label', String, queue_size=1)
	#Defining the publisher

	#global pub
	#pub = rospy.Publisher('/pose', geometry_msgs.msg.PointStamped, queue_size = 10)
	
	#Gripper command publisher
	gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)
	#Contact Sensors Subscribers
	sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
	sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
	cb = message_filters.TimeSynchronizer([sub1, sub2], 10)
	cb.registerCallback(callback)

	rospy.Subscriber('/pose', geometry_msgs.msg.PoseStamped, yolo_cb)

	#Getting camera info
	print("Running")
	camera_info = rospy.wait_for_message('/kinect/color/camera_info', CameraInfo)
	print("Got Cam")
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