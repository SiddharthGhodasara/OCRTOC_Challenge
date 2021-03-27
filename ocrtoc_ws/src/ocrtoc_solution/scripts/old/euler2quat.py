#! /usr/bin/env python

import actionlib
import rospy

import ocrtoc_task.msg
from control_msgs.msg import GripperCommandActionGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

#Our Imported Libraries
import tf
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