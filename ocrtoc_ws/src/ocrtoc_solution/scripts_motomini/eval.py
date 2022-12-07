#! /usr/bin/env python

#Importing Libraries
import rospy
import actionlib
import ocrtoc_task.msg
import actionlib
import rospy
import ocrtoc_task.msg
import math
import time

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

		# create messages that are used to publish feedback/result.
		self.feedback = ocrtoc_task.msg.CleanFeedback()
		self.result = ocrtoc_task.msg.CleanResult()

		# get models directory.
		materials_path = rospy.get_param('~materials_dir','~/ocrtoc_materials')
		self.models_dir = materials_path + '/models'
		rospy.loginfo("Models dir: " + self.models_dir)

	def execute_callback(self, goal):
		#Defining the use of global variables
		rospy.loginfo("Get clean task.")
		
		self.result.status = "Finished"
		rospy.loginfo("Done.")
		self.action_server.set_succeeded(self.result)

#Main Thread
if __name__ == '__main__':
	#Initializing the node
	rospy.init_node('commit_solution_eval')

    #Calling the task class
	commit_solution = CommitSolution('commit_solution')
	print("Here")
	rospy.spin()
