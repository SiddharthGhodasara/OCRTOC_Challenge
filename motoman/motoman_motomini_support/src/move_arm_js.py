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
	#pub = rospy.Publisher('joint_states', JointState, queue_size=1)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((HOST, PORT))
	js = arm_group.get_current_joint_values()
	#print(js)
	move_arm(js)
	print(arm_group.get_current_pose())
	#rospy.Subscriber('/joint_states', JointState, callback)
	rospy.spin()

	
