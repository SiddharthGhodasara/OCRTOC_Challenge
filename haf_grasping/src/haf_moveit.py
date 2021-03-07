#! /usr/bin/env python
import rospy
import sys
import copy
import tf
import tf2_ros
import tf2_geometry_msgs
import time
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from agile_grasp.msg import Grasps
import agile_grasp.msg
from std_msgs.msg import Header, Int64
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PointStamped
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal
from visualization_msgs.msg import MarkerArray
from control_msgs.msg import GripperCommandActionGoal
from std_msgs.msg import String
from tf.transformations import quaternion_from_euler
from gazebo_msgs.msg import ContactsState

moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('select_grasp_new',anonymous=True)
grasps_plots = ""
tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
tf_listener = tf2_ros.TransformListener(tf_buffer)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm_controller")
group_1 = moveit_commander.MoveGroupCommander("gripper_controller")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)

contact = None
def callback(msg):
    global contact
    contact= msg.states

sub = rospy.Subscriber('/finger1_contact_sensor_state', ContactsState, callback)

yolo_pose = rospy.wait_for_message('/pose', PointStamped)
print(yolo_pose.header.frame_id)

obj1_x = yolo_pose.point.x
obj1_y = yolo_pose.point.y
obj1_z = yolo_pose.point.z


def callback_plots(msg_plots):
	global grasps_plots
	grasps_plots = msg_plots.data.split(" ")
	# print grasps_plots

grasps_plots_sub = rospy.Subscriber('/haf_grasping/grasp_hypothesis_with_eval', String, callback_plots)

# Wait for gsps to arrive.
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	if grasps_plots != "" :
		if int(grasps_plots[0]) > 70:
			print("satisfied grasp condition")
			print(int(grasps_plots[0]))
			break

	else:
		print("searching again for better grasp")
		rate.sleep()


position_x = float(grasps_plots[-4])
position_y = float(grasps_plots[-3])
position_z = float(grasps_plots[-2])

roll = float(grasps_plots[-1])
print(grasps_plots[-1])
print(roll)
r,p,y= (roll - 90 ,90,0)
grasp_pose = geometry_msgs.msg.PoseStamped()
grasp_pose.header.frame_id = "/world"

grasp_pose.pose.position.x = position_x
grasp_pose.pose.position.y = position_y
grasp_pose.pose.position.z = position_z + 0.1

r_rad = (r*3.14159265358979323846)/180
p_rad = (p*3.14159265358979323846)/180
y_rad = (y*3.14159265358979323846)/180
   #print(r1,p1,y1)
q = quaternion_from_euler(r_rad,p_rad,y_rad)

print "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])

grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

'''
target_frame = "world"
source_frame = "base_link"
transform = tf_buffer.lookup_transform(target_frame,
                                       source_frame, #source frame
                                       rospy.Time(0), #get the tf at first available time
                                       rospy.Duration(5.0)) #wait for 1 second

pose_transformed = tf2_geometry_msgs.do_transform_pose(grasp_pose, transform)
# print(pose_transformed)

pose_target = geometry_msgs.msg.PoseStamped()
pose_target.header.frame_id = "world"

pose_z = pose_transformed.pose.position.z
# br.sendTransform(position, orientation,rospy.Time.now(), "world", "kinect_optical_frame" )
pose_target.pose.position.x =  pose_transformed.pose.position.x + 0.005	#grasps[0].position.x
pose_target.pose.position.y =  pose_transformed.pose.position.y  #grasps[0].position.y
pose_target.pose.position.z =  pose_z + 0.1 #grasps[0].position.z

pose_target.pose.orientation.x = pose_transformed.pose.orientation.x
pose_target.pose.orientation.y = pose_transformed.pose.orientation.y
pose_target.pose.orientation.z = pose_transformed.pose.orientation.z
pose_target.pose.orientation.w = pose_transformed.pose.orientation.w

print(pose_transformed.pose)
'''
group.set_planning_time(50)
group.set_pose_target(grasp_pose)

plan2 = group.plan()
group.go(wait=True)
rospy.sleep(1)

gripper_cmd = GripperCommandActionGoal()
gripper_cmd.goal.command.position = 0.04
gripper_cmd.goal.command.max_effort = 0.0
gripper_cmd_pub.publish(gripper_cmd)
rospy.loginfo("Pub gripper_cmd")
rospy.sleep(1.0)


grasp_pose.pose.position.z =  position_z
group.set_pose_target(grasp_pose)
group.go(wait=True)

rospy.sleep(1)

rate = rospy.Rate(30)

cmd = 0.039
while not rospy.is_shutdown():
    if len(contact)>0:
       print(contact)
       break
    gripper_cmd.goal.command.position = cmd
    gripper_cmd.goal.command.max_effort = 0.01
    gripper_cmd_pub.publish(gripper_cmd)
    cmd -= 0.001
    rate.sleep()

grasp_pose.pose.position.z = position_z + 0.1
group.set_pose_target(grasp_pose)
group.go(wait=True)

print("DOne")

moveit_commander.roscpp_shutdown()
