#! /usr/bin/env python

import rospy
from shapely.geometry import Polygon

class Swap:

	#Function to check if swapping is needed
	def check(self, req_obj, i, pose_list, size_list, goal):

		obj_h = size_list[req_obj][0] #* float(goal.scale_list[tc])
		obj_w = size_list[req_obj][1] #* float(goal.scale_list[tc])

		goal_x1, goal_y1 = goal.pose_list[i].position.x - obj_w/2, goal.pose_list[i].position.y - obj_h/2
		goal_x2, goal_y2 = goal.pose_list[i].position.x - obj_w/2, goal.pose_list[i].position.y + obj_h/2
		goal_x3, goal_y3 = goal.pose_list[i].position.x + obj_w/2, goal.pose_list[i].position.y - obj_h/2
		goal_x4, goal_y4 = goal.pose_list[i].position.x + obj_w/2, goal.pose_list[i].position.y + obj_h/2

		box_1 = [[goal_x1, goal_y1], [goal_x2, goal_y2], [goal_x4, goal_y4], [goal_x3, goal_y3]]
		print("box 1: ", box_1)
		poly_1 = Polygon(box_1)

		#Get the current coordinates of all other objects
		for j in range(0, len(goal.object_list)):
			#Ignoring current object
			if j == i: 
				print("No intersection")
				continue

			label = goal.object_list[j]
			pose = pose_list[label]

			if (pose == None):
				j+=1
				continue

			#length and width of object
			w = size_list[label][0]
			h = size_list[label][1]

			#Getting Current pose
			x = pose.pose.position.x
			y = pose.pose.position.y

			x1, y1 = x - w/2, y - h/2
			x2, y2 = x - w/2, y + h/2
			x3, y3 = x + w/2, y - h/2
			x4, y4 = x + w/2, y + h/2
			box_2 = [[x1, y1], [x2, y2], [x4, y4], [x3, y3]]
			print("box 2: ", box_2)
			poly_2 = Polygon(box_2)

			#self.swap = 0
			#Check for intersection
			print("Intersection area: ", poly_1.intersection(poly_2).area)
			if poly_1.intersection(poly_2).area != 0:

				#swap_name = goal.object_list[j]
				goal.object_list[i], goal.object_list[j] = goal.object_list[j],goal.object_list[i]
				goal.pose_list[i].position.x , goal.pose_list[j].position.x = goal.pose_list[j].position.x , goal.pose_list[i].position.x
				goal.pose_list[i].position.y, goal.pose_list[j].position.y = goal.pose_list[j].position.y, goal.pose_list[i].position.y
				goal.pose_list[i].position.z, goal.pose_list[j].position.z = goal.pose_list[j].position.z, goal.pose_list[i].position.z
					
				goal.pose_list[i].orientation.x , goal.pose_list[j].orientation.x = goal.pose_list[j].orientation.x , goal.pose_list[i].orientation.x 
				goal.pose_list[i].orientation.y , goal.pose_list[j].orientation.y = goal.pose_list[j].orientation.y , goal.pose_list[i].orientation.y
				goal.pose_list[i].orientation.z , goal.pose_list[j].orientation.z = goal.pose_list[j].orientation.z , goal.pose_list[i].orientation.z
				goal.pose_list[i].orientation.w , goal.pose_list[j].orientation.w = goal.pose_list[j].orientation.w , goal.pose_list[i].orientation.w
				return goal,i
		return goal,i