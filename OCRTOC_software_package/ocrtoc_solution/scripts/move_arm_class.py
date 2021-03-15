#!/usr/bin/env python

#Importing Libraries
import sys
import math
import rospy
import serial
import socket
import moveit_commander 
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped

moveit_commander.roscpp_initialize(sys.argv)

HOST = '192.168.255.1'  # The server's hostname or IP address
PORT = 11000        # The port used by the server

arm_group = moveit_commander.MoveGroupCommander("arm")
#hand_group= moveit_commander.MoveGroupCommander("gripper")

class move_arm:
    def __init__(self):
        #rospy.init_node('move_arm_motomini___node', anonymous=True)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect((HOST, PORT))
        self.ser = serial.Serial('/dev/ttyACM3', baudrate = 9600, timeout = 1)

    def arm_go(self):
        valpos = arm_group.get_current_joint_values()
        print("Moving")
        for i in range(len(valpos)):
            valpos[i] = math.degrees(valpos[i]) * 10000

        print("Val Pose" , valpos)
        sendval = 'MOVE REL X ' + str(long(valpos[0])) + ' Y '+ str(long(valpos[1])) +' Z '+ str(long(valpos[2])) +' RX '+ str(long(valpos[3])) +' RY '+ str(long(valpos[4])) +' RZ '+ str(long(valpos[5])) +' SPEED 0.78\n'
        self.s.sendall(str.encode(sendval))
        data = self.s.recv(1024)
        print(data)

        return

    def  gripper_go(self, cmd):
        print("open")
        cmd_bytes = bytes(cmd)
        self.ser.write(cmd_bytes)
