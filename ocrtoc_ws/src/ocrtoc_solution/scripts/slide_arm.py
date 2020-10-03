#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander 
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
import message_filters
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal
#from grasp_ros.msg import GraspConfigList
from tf.transformations import quaternion_from_euler
from control_msgs.msg import GripperCommandActionGoal
from control_msgs.msg import GripperCommandAction
from control_msgs.msg import GripperCommandGoal
from gazebo_msgs.msg import ContactsState
from geometry_msgs.msg import Wrench

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_python_node',anonymous=True)

robot = moveit_commander.RobotCommander()  
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm_controller")
group1 = moveit_commander.MoveGroupCommander("gripper_controller")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)




pose_target = geometry_msgs.msg.Pose()

group.set_named_target("pose1")
plan3 = group.go(wait=True)

group.set_named_target("slide_pose_assist")
plan3 = group.go(wait=True)


group.set_named_target("slide_pose_main")
plan3 = group.go(wait=True)

waypoints = []
scale=1
wpose = group.get_current_pose().pose
wpose.position.x += scale * 0.15  
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)

#rospy.sleep(1)

#pose_target.position.z =  0.0226+0.1
#group.set_pose_target(pose_target)
#group.go(wait=True)
waypoints = []
wpose = group.get_current_pose().pose
wpose.position.z += scale * 0.15
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)


group.set_named_target("pose1")
plan3 = group.go(wait=True)

#rospy.sleep(2)
#print(group.get_current_pose())


moveit_commander.roscpp_shutdown()

