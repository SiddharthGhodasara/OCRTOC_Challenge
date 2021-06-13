#! /usr/bin/env python

import tf
import sys
import math
import time
import copy
import rospy
import actionlib
from control_msgs.msg import GripperCommandActionGoal
import moveit_msgs.msg
import moveit_commander 
import geometry_msgs
import tf.transformations
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, JointConstraint, Constraints
import tf2_ros 
import tf2_geometry_msgs
import message_filters
from gazebo_msgs.msg import ContactsState
from std_msgs.msg import *


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
		self.arm_group = moveit_commander.MoveGroupCommander("arm_controller")
		self.hand_group = moveit_commander.MoveGroupCommander("gripper_controller")
		self.gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)
		self.rs_state_pub = rospy.Publisher('/realsense_state', Float32, queue_size=10)
		self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)

		#Contact Sensors Subscribers
		self.retry = 0
		self.sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
		self.sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
		self.cb = message_filters.TimeSynchronizer([self.sub1, self.sub2], 10)
		self.cb.registerCallback(self.callback)
		
	
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
			pose_target = "pose1"
			print("moveit pose: ", pose_target)
			self.arm_group.set_named_target(pose_target)
			self.arm_group.set_planning_time(20)
			#plan = arm_group.plan()
			self.arm_group.go(wait=True)
			
	



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
    
	def gripper_state(self, state):
		if(state=='open'):
			self.hand_group.set_named_target("gripper_open")
			self.hand_group.go(wait=True)
			return 1
		
		elif(state=='gripper_close'):
			self.hand_group.set_named_target("gripper_close")
			self.hand_group.go(wait=True)
			return 1
			
		else:
			gripper_cmd = GripperCommandActionGoal()
			cmd = 0.039
			closure = -1
			while not rospy.is_shutdown():
				#Checking if both grippers are touching the object
				if len(self.contact1)>0 and len(self.contact2)>0:
					closure = 1
					self.retry = 0
					break

				
				#Checking if we are not reached the lower closinhg limit
				if cmd > 0.0002:
					gripper_cmd.goal.command.position = cmd
					gripper_cmd.goal.command.max_effort = 0.01
					self.gripper_cmd_pub.publish(gripper_cmd)
					cmd -= 0.0004
					rospy.Rate(20).sleep()

				#Re do the task if the lower limit is reached
				else:
					closure = 0
					break

			if (closure == 0 and self.retry < 3): 

				print("Missed object, going back to initial pose and trying again")
				#Opening the gripper
				self.hand_group.set_named_target("gripper_open")
				self.hand_group.go(wait=True)

				#Moving up from the placing location
				self.waypoints(0.15)
				rospy.sleep(1)

				#Closing the gripper back
				self.hand_group.set_named_target("gripper_close")
				self.hand_group.go(wait=True)

				#Going back to pose1
				self.arm_group.set_named_target("pose1")
				self.arm_group.go(wait=True)
				self.retry+=1
				return -1
				
			if(self.retry>=3):    
				self.retry = 0
				return -2
				
			else:    
				return 1 
