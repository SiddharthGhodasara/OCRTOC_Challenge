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


#grasps = []
contact1 = None
contact2 = None
def callback(msg1,msg2):
    global contact1
    global contact2
    #print("In callback")
    
    contact1= msg1.states
    contact2= msg2.states
    #if len(contact1)>0 and len(contact2)>0:
       #print("Detected contact")
       #force1= msg1.states.total_wrench.force 


sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
cb = message_filters.TimeSynchronizer([sub1, sub2], 10)
cb.registerCallback(callback)
#rospy.spin()


pose_target = geometry_msgs.msg.Pose()
pose_target.position.x =  -0.066958 #0.245# ##-0.28#3155924902#0.0455312686019
pose_target.position.y =  0.349095#0.108##-0.03#83420782723#0.463301607729
pose_target.position.z =  0.009951+0.1#0.0226+0.1##0.399089506#0.391596235061

r,p,y= (90,90,0) #deg
r_rad = (r*3.14159265358979323846)/180
p_rad = (p*3.14159265358979323846)/180
y_rad = (y*3.14159265358979323846)/180
#print(r1,p1,y1)
q = quaternion_from_euler(r_rad,p_rad,y_rad)
 
print "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])

pose_target.orientation.x = q[0]#-0.000120072221133#q[0]#0.0330125155885#0.5#1#-0.656609466283
pose_target.orientation.y = q[1]#0.70707496883#q[1]#-0.0219063748305#-0.5# 0.409955979071
pose_target.orientation.z = q[2]#0.000267048607595#q[2]#0.535765919038#0.5# 0.576088018764
pose_target.orientation.w = q[3]#0.707138531493#q[3]#.843436520761#0.5#0.262531328891
#print(pose_target)
#group.set_goal_orientation_tolerance (0.09)
#group.set_goal_position_tolerance (0.01)
#group.set_goal_tolerance(0.003)
#group.set_planning_attempts(20)
group.set_planning_time(50)
group.set_pose_target(pose_target)
plan2 = group.plan()
rospy.sleep(2)
group.go(wait=True)


group1.set_named_target("gripper_open")
plan3 = group1.go(wait=True)
rospy.loginfo("Opening Gripper")


waypoints = []
scale=1
wpose = group.get_current_pose().pose
wpose.position.z -= scale * 0.1  
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)

rospy.sleep(1)

gripper_cmd = GripperCommandActionGoal()
rate = rospy.Rate(20)
cmd = 0.039
while not rospy.is_shutdown():
    if len(contact1)>0 and len(contact2)>0:
       print("Detected contact")
       #print("Contact2", contact2)
       break
    #group_variable_values = group1.get_current_joint_values()
    #group_variable_values[0] = cmd
    #group_variable_values[1] = 0.05
    #group1.set_joint_value_target(group_variable_values)
    #group1.go(wait=True)
    if cmd > 0.005:
       gripper_cmd.goal.command.position = cmd
       gripper_cmd.goal.command.max_effort = 0.01
       gripper_cmd_pub.publish(gripper_cmd)
       print(cmd)
       
       cmd -= 0.0005
       rate.sleep()
#print(cmd)


#pose_target.position.z =  0.0226+0.1
#group.set_pose_target(pose_target)
#group.go(wait=True)
waypoints = []
wpose = group.get_current_pose().pose
wpose.position.z += scale * 0.1
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)

#pose_target.position.z =  0.0226
#group.set_pose_target(pose_target)
#group.go(wait=True)
waypoints = []
wpose = group.get_current_pose().pose
wpose.position.z -= scale * 0.1
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)

'''
waypoints = []

wpose = group.get_current_pose().pose
wpose.position.z -= scale * 0.1  # First move up (z)
#wpose.position.y += scale * 0.2  # and sideways (y)
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)

group.execute(cartesian_plan, wait=True)
'''


group1.set_named_target("gripper_open")
plan3 = group1.go(wait=True)
rospy.loginfo("Pub gripper_cmd")
rospy.sleep(1.0)


#pose_target.position.z =  0.0226+0.1
#group.set_pose_target(pose_target)
#group.go(wait=True)
waypoints = []
wpose = group.get_current_pose().pose
wpose.position.z += scale * 0.1
waypoints.append(copy.deepcopy(wpose))
(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
group.execute(cartesian_plan, wait=True)


group1.set_named_target("gripper_close")
plan3 = group1.go(wait=True)
rospy.sleep(1)
group.set_named_target("task_pose")
plan3 = group.go(wait=True)


#print(group.get_current_pose())


moveit_commander.roscpp_shutdown()

