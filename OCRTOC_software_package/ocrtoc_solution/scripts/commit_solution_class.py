#! /usr/bin/env python


#Importing Libraries
import rospy
import actionlib
import ocrtoc_task.msg
import actionlib
import rospy
from control_msgs.msg import GripperCommandActionGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math

from do_task_yrc import do_task

#Solution Class
class CommitSolution(object):
	def __init__(self, name):
		# Init action.
		self.action_name = name
		self.action_server = actionlib.SimpleActionServer(
			self.action_name, ocrtoc_task.msg.CleanAction,
			execute_cb=self.execute_callback, auto_start=False)
		self.action_server.start()
		rospy.loginfo(self.action_name + " is running.")

		self.arm_cmd_pub = rospy.Publisher(
			rospy.resolve_name('arm_controller/command'), JointTrajectory, queue_size=10)

		self.gripper_cmd_pub = rospy.Publisher(
			rospy.resolve_name('gripper_controller/gripper_cmd/goal'), GripperCommandActionGoal, queue_size=10)

		# create messages that are used to publish feedback/result.
		self.feedback = ocrtoc_task.msg.CleanFeedback()
		self.result = ocrtoc_task.msg.CleanResult()

		# get models directory.
		materials_path = rospy.get_param('~materials_dir','/root/ocrtoc_materials')
		self.models_dir = materials_path + '/models'
		rospy.loginfo("Models dir: " + self.models_dir)

	def execute_callback(self, goal):
		#Defining the use of global variables
		rospy.loginfo("Get clean task.")

		task_var = do_task()
		i = 0
		while(i<len(goal.object_list)):
			goal, i = task_var.task(goal, i)
			rospy.sleep(5)

		print("Going for 1st feedback")
		for i in range(len(goal.object_list)):
			feedback_res = task_var.feedback(goal,i)

		print("Going for final feedback")
		for i in range(len(goal.object_list)):
			feedback_res = task_var.feedback(goal,i)
			
		print("Done with feedback")

		#self.result.status = "Finished"
		rospy.loginfo("Done.")
		#self.action_server.set_succeeded(self.result)

#Main Thread
if __name__ == '__main__':
	#Initializing the node
	rospy.init_node('commit_solution')

    #Calling the task class
	commit_solution = CommitSolution('commit_solution')
	print("Here")
	rospy.spin()