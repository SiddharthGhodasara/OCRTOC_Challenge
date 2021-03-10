#!/usr/bin/env python

#Importing Libraries
import rospy
import moveit_msgs.msg
import moveit_commander
from geometry_msgs.msg import PoseStamped

# Initializing rospy node
rospy.init_node('yolo_moveit',anonymous=True)

# Instantiating a RobotCommander object. This provides information on robot's current joint states.
robot = moveit_commander.RobotCommander() 

# Instantiating a PlanningScene object(provides info on obtaining and updating robot's understanding of the world)
scene = moveit_commander.PlanningSceneInterface()

# Instantiating a MoveGroupCommander object. This object is an interface to a planning group.
arm_group = moveit_commander.MoveGroupCommander("arm")

# Create a DisplayTrajectory ROS publisher (used to display trajectories in Rviz)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)


def callback(pose_target):
    
    #print(pose)
	
    # Specifying the target pose to the planning group of the robot.
	pose_target.header.frame_id = "world"
	
	curr_pose = arm_group.get_current_pose()
	print(curr_pose)
	
	pose_target.pose.position.z += 0.1
	#pose_target.pose.position.x =  0.08349
	#pose_target.pose.position.y = 0.0
	#pose_target.pose.position.z = 0.228
	
	pose_target.pose.orientation.x = 1#curr_pose.pose.orientation.x
	pose_target.pose.orientation.y = 0#curr_pose.pose.orientation.y
	pose_target.pose.orientation.z = 0#curr_pose.pose.orientation.z
	pose_target.pose.orientation.w = 0#curr_pose.pose.orientation.w
	
	print(pose_target)
	arm_group.set_pose_target(pose_target)
	# Giving the robot a maximum planning time 20 sec to plan its path.
	arm_group.set_planning_time(20)
	# Planning a path to reach the location
	plan1 = arm_group.plan()
	# Executing the path
	arm_group.go(wait=True)


if __name__ == "__main__":
    rospy.Subscriber('/pose', PoseStamped, callback)
    rospy.spin()
