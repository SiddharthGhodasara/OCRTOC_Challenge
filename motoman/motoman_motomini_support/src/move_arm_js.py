#!/usr/bin/env python

#Importing Libraries 158855 -185926
import rospy
import math
import socket
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped

import sys
import copy
import rospy
import math
import tf
import time
import moveit_commander 
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib

import tf 
from tf.transformations import * 
import tf2_ros
import tf2_geometry_msgs

from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, JointConstraint, Constraints

moveit_commander.roscpp_initialize(sys.argv)

HOST = '192.168.255.1'  # The server's hostname or IP address
PORT = 11000        # The port used by the server
M_PI = math.pi
s = None
js_old = [0, 0, 0, 0, 0, 0]


robot = moveit_commander.RobotCommander()  
scene = moveit_commander.PlanningSceneInterface()

arm_group = moveit_commander.MoveGroupCommander("arm")
#hand_group= moveit_commander.MoveGroupCommander("gripper")


display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)

#Tranform Listener
tf_listener = None
#Transformations
tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length



def move_arm(valpos):
	print("Moving")
	for i in range(len(valpos)):
		valpos[i] = math.degrees(valpos[i]) * 10000
	print("Val Pose" , valpos)
	sendval = 'MOVE REL X ' + str(long(valpos[0])) + ' Y '+ str(long(valpos[1])) +' Z '+ str(long(valpos[2])) +' RX '+ str(long(valpos[3])) +' RY '+ str(long(valpos[4])) +' RZ '+ str(long(valpos[5])) +' SPEED 0.78\n'
	#print(sendval)
	s.sendall(str.encode(sendval))
	data = s.recv(1024)
	print(data)

def callback(pose):
    global js_old
    js = list(pose.position)
    print("Got JS", js)
    
    #if js_old == js:
    	#print("Got last pose")
    move_arm(js)
    #else:
        #js_old = js[:]



if __name__ == "__main__":
	global s
	rospy.init_node('move_arm_node')
	
	tf_listener = tf2_ros.TransformListener(tf_buffer)
	
	#pub = rospy.Publisher('joint_states', JointState, queue_size=1)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((HOST, PORT))
	js = arm_group.get_current_joint_values()
	#print(js)
	move_arm(js)
	pose = arm_group.get_current_pose()
	
	print(pose)
	
	target_frame = "link_1_s"
	source_frame = "world"
	transform = tf_buffer.lookup_transform(target_frame, 
		source_frame, #source frame
		rospy.Time(0), #get the tf at first available time
		rospy.Duration(1.0)) #wait for 1 second

    	#Applying the transform
	rs_pose = tf2_geometry_msgs.do_transform_pose(pose, transform)
    	
    	print(transform)
    	
	quat = [rs_pose.pose.orientation.x, rs_pose.pose.orientation.y, rs_pose.pose.orientation.z, rs_pose.pose.orientation.w]
    	print(rs_pose)
	r,p,y = euler_from_quaternion(quat, axes='sxyz')
	print("Roll", r)
	print("Pitch", p)
	print("Yaw", y)
	#rospy.Subscriber('/joint_states', JointState, callback)
	rospy.spin()

	
