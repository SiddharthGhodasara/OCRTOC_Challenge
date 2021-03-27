#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

from tf.transformations import euler_from_quaternion, quaternion_from_euler 
import numpy as np
import math

import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import *


def transform(x,y,z,x1,y1,z1,w1):
    #q = quaternion_from_euler(r, p, y)
    grasp_pose = geometry_msgs.msg.PoseStamped()
    grasp_pose.header.frame_id = '/kinect_optical_frame'

    grasp_pose.pose.position.x = x
    grasp_pose.pose.position.y = y
    grasp_pose.pose.position.z =z

    grasp_pose.pose.orientation.x = x1#q[0]
    grasp_pose.pose.orientation.y = y1#q[1]
    grasp_pose.pose.orientation.z = z1#q[2]
    grasp_pose.pose.orientation.w = w1#q[3]

    print(type(grasp_pose))
    #transfromed_grasp_pose = transformPose(target_frame, grasp_pose)
    #print(transfromed_grasp_pose)
    tgt_frame = "world"
    src_frame = "kinect_optical_frame"
    transform = tf_buffer.lookup_transform(tgt_frame, src_frame, rospy.Time(0), rospy.Duration(1.0)) #wait for 1 second

    pose_transformed = tf2_geometry_msgs.do_transform_pose(grasp_pose, transform)
    x_p = pose_transformed.pose.position.x
    y_p = pose_transformed.pose.position.y
    z_p = pose_transformed.pose.position.z

    x_or = pose_transformed.pose.orientation.x 
    y_or = pose_transformed.pose.orientation.y 
    z_or = pose_transformed.pose.orientation.z 
    w_or = pose_transformed.pose.orientation.w
    print(x_p,y_p,z_p)
    print(euler_from_quaternion([x_or,y_or,z_or,w_or]))


if __name__ == '__main__':
    try:
        rospy.init_node('commit_solution')
        tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length
        tf_listener = tf2_ros.TransformListener(tf_buffer)
        transform(-0.090104 , 0.071906, 0.759602,   0.617387 , -0.344721, 0.617387 , -0.344721)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
