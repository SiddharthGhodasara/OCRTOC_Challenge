#! /usr/bin/env python

import tf
import sys
import math
import time
import copy
import rospy
import tf2_ros 
import actionlib
import geometry_msgs
import message_filters
import moveit_msgs.msg
import moveit_commander 
import tf2_geometry_msgs
import tf.transformations
from std_msgs.msg import *
from gazebo_msgs.msg import ContactsState
from move_arm_class import move_arm as real_arm
from control_msgs.msg import GripperCommandActionGoal
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, JointConstraint, Constraints


class Arm:
	
    # Initializing all varibales, publishers and subscribers
	def __init__(self):

		# Initalising the moveit commander
		moveit_commander.roscpp_initialize(sys.argv)

		# Initialising publishers, moveit controllers and other required things
		self.tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
		self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

		# Moveit Initializtion
		self.robot = moveit_commander.RobotCommander()
		self.scene = moveit_commander.PlanningSceneInterface()
		self.arm_group = moveit_commander.MoveGroupCommander("arm")
		#self.hand_group = moveit_commander.MoveGroupCommander("gripper_controller")
		#self.gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)
		self.rs_state_pub = rospy.Publisher('/realsense_state', Float32, queue_size=10)
		self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)

		#Contact Sensors Subscribers
		self.retry = 0
		#self.sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
		#self.sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
		#self.cb = message_filters.TimeSynchronizer([self.sub1, self.sub2], 10)
		#self.cb.registerCallback(self.callback)

		#Connecting real arm through sockets
		self.yrc_controller = real_arm()
		
	
	#Function for getting contact sensors data
	def callback(self, msg1, msg2):
		self.contact1 = msg1.states
		self.contact2 = msg2.states

        
	def move_arm(self, pose_quat=None, pose_rpy=None, pose_type=0, offset=None):
		# pose_type =  0->pose_quat  1->pose_rpy  2->named_pose
		# Pose message		
		if(pose_type== 1):
			pose_target = geometry_msgs.msg.PoseStamped()
			pose_target.header.frame_id = "world"
			pose_target.pose.position.x = pose_rpy[0] + offset[0]
			pose_target.pose.position.y = pose_rpy[1] + offset[1]
			pose_target.pose.position.z = pose_rpy[2] + offset[2]
			quat = tf.transformations.quaternion_from_euler(pose_rpy[3]+offset[3], pose_rpy[4]+offset[4], pose_rpy[5]+offset[5])
			pose_target.pose.orientation.x = quat[0]
			pose_target.pose.orientation.y = quat[1]
			pose_target.pose.orientation.z = quat[2]
			pose_target.pose.orientation.w = quat[3]
			print("moveit pose: ", pose_target)
			self.arm_group.set_pose_target(pose_target)
			self.arm_group.set_planning_time(20)
			#plan = arm_group.plan()
			self.arm_group.go(wait=True)
			
		elif(pose_type== 0):
			pose_target = geometry_msgs.msg.PoseStamped()
			pose_target.header.frame_id = "world"
			pose_target.pose.position.x = pose_quat.pose.position.x + offset[0]
			pose_target.pose.position.y = pose_quat.pose.position.y + offset[1]
			pose_target.pose.position.z = pose_quat.pose.position.z + offset[2]
			pose_target.pose.orientation.x = pose_quat.pose.orientation.x
			pose_target.pose.orientation.y = pose_quat.pose.orientation.y
			pose_target.pose.orientation.z = pose_quat.pose.orientation.z
			pose_target.pose.orientation.w = pose_quat.pose.orientation.w
			print("moveit pose: ", pose_target)
			self.arm_group.set_pose_target(pose_target)
			self.arm_group.set_planning_time(20)
			#plan = arm_group.plan()
			self.arm_group.go(wait=True)
				
		else:
			pose_target = "init_pose"
			print("moveit pose: ", pose_target)
			self.arm_group.set_named_target(pose_target)
			self.arm_group.set_planning_time(20)
			#plan = arm_group.plan()
			self.arm_group.go(wait=True)
			
		x = raw_input("Input")
		self.yrc_controller.arm_go()
		
		rospy.sleep(5)



		#print(arm_group.get_current_joint_values())
		#print(arm_group.get_current_pose())

		#moveit_commander.roscpp_shutdown()
	
	
	def waypoints(self, distance):
		waypoints = []
		wpose = self.arm_group.get_current_pose().pose
		wpose.position.z +=  distance
		waypoints.append(copy.deepcopy(wpose))
		(cartesian_plan, fraction) = self.arm_group.compute_cartesian_path(waypoints,0.01, 0.0)
		self.arm_group.execute(cartesian_plan, wait=True)
		self.yrc_controller.arm_go()
		rospy.sleep(2)
    
	def gripper_state(self, state):
		if(state=='open'):
			h = self.yrc_controller.gripper_go('o')
			return 1
		
		elif(state=='close'):
			value = self.yrc_controller.gripper_go('c')
			print(int(value))
			if int(value) < 80:
				print("Grasping Failed! Redo Grapsing")

				if self.retry < 3: 

					print("Missed object, going back to initial pose and trying again")
					#Opening the gripper
					self.gripper_state("open")

					#Moving up from the placing location
					self.waypoints(0.07)
					rospy.sleep(1)

					#Going back to pose1
					self.move_arm(pose_type=2)
					return -1
				
			if(self.retry>=3):    
				self.retry = 0
				return -2
				
			else:    
				return 1
		else:
			print("None") 
