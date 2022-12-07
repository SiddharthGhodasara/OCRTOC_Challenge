#! /usr/bin/env python

#Importing libraries
import math
import rospy
import numpy as np
from tf.transformations import euler_from_quaternion


#Importing custom clases
from move import Arm
from swap import Swap
from grasping import Grasping
from perception import Perception


class do_task:

    #Initializing all varibales, publishers and subscribers
    def __init__(self):

        #Initalizing varibales used
		self.obj_pose = {}
		self.obj_size = {}
        
        #Defining Class Objects
		self.check_swap = Swap()
		self.motion_planning = Arm()
		self.grasping_obj = Grasping()
		self.preception_obj = Perception(image_topic = "/camera/rgb/image_raw", depth_topic = "/camera/depth_registered/image", camera_frame = "camera_rgb_optical_frame", camera_topic = "/camera/rgb/camera_info")

		#Opening the gripper
		#self.motion_planning.gripper_state('open')
		#Going the task pose
		self.motion_planning.move_arm(pose_type = 2)



    def feedback(self, goal, i): 

        print("Evaluating feedback")

        name = goal.object_list[i]
        
        #Sending to YOLO and getting output coordinates
        obj_pose = self.preception_obj.predict(name)

        if (obj_pose == None):
            #i+=1
            print("Object not detected by YOLO, skipping " +  name)
            return -1 
			

        #Extracting pose of current object
        pose_curr_x = obj_pose.pose.position.x
        pose_curr_y = obj_pose.pose.position.y

        #(r1,p1,y1) = euler_from_quaternion(pose.pose.orientation, axes='sxyz')
        #(r2,p2,y2) = euler_from_quaternion(goal.pose_list[i].orientation, axes='sxyz')
        #print("Error in rpy: ")
        #print((r2-r1), (p2-p1), (y2-y1))
        
        #Checking if threshold is within threshold
        if abs(pose_curr_x - goal.pose_list[i].position.x) <= 0.10 and abs(pose_curr_y - goal.pose_list[i].position.y) <= 0.10:

            print("Good Job Translation for {}".format(name))
            return 1

        #If not within the threshold, do that object again
        else:
            print("Bad Job Translation for {}".format(name))
            goal, i = self.task(goal, i)
            return 0

    def task(self, goal, i):

		
		#Getting the goal details
		name = str(goal.object_list[i])
		goal_x = goal.pose_list[i].position.x
		goal_y = goal.pose_list[i].position.y

		#Getting the size and 3D pose of all objects
		for obj in goal.object_list:
			self.obj_size[obj] = self.preception_obj.get_dim(obj)
			self.obj_pose[obj] = self.preception_obj.predict(obj)

		goal,i = self.check_swap.check(name, i, self.obj_pose, self.obj_size, goal)
		
		#Getting the new goal details
		name = str(goal.object_list[i])
		goal_x = goal.pose_list[i].position.x
		goal_y = goal.pose_list[i].position.y
		
		#Getting the required objects position
		obj_pose = self.preception_obj.predict(name)
		#print('Yolos pose:', obj_pose)
		if (obj_pose is None):
			i+=1
			print("Object not detected by YOLO, skipping " +  name)
			return goal, i


		''' Real World Offset '''
		# For hovering the realsense directly above the objects
		tot_distance = (obj_pose.pose.position.x**2 + obj_pose.pose.position.y**2)**0.5  
		# For nearby objects, offset is lesser
		req_distance = tot_distance - 0.06 #0.02 
		z=0.18
		pitch = 1.37 #1.06
		
		print("REQUIRED DISTANCE",tot_distance)
		'''if (tot_distance > 0.23):
			print("Increasing height of arm")
			z = 0.20
			pitch = 1.06
			req_distance = tot_distance - 0.14 #0.1  # For far objects, offset is more
		'''
		x_back = req_distance * math.cos(math.atan2(obj_pose.pose.position.y, obj_pose.pose.position.x))
		y_back = req_distance * math.sin(math.atan2(obj_pose.pose.position.y, obj_pose.pose.position.x))
		
		position_list = [x_back, y_back, z, 0.0, pitch, math.atan2(obj_pose.pose.position.y-0.01, obj_pose.pose.position.x)]
		''' Ending Block '''


		self.motion_planning.move_arm(pose_rpy = position_list, offset = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], pose_type = 1)

		#Getting the grasp coordinates
		grasp_pose = self.grasping_obj.get_grasps_coord(obj_pose)
		#grasp_pose.pose.position.z = goal.pose_list[i].position.z * 2.4
		
		xx = raw_input("INput")
		self.motion_planning.move_arm(pose_quat = grasp_pose, offset = [0,0,0], pose_type = 0)

		#Opening the gripper
		self.motion_planning.gripper_state('open')
		
		print(name)
		if name not in ['banana', 'mug', 'screwdriver']:
			x = raw_input("Go down")
			#Going Down to pick object
			self.motion_planning.waypoints(-0.02)

		x = raw_input("Close")
		#Closing the gripper
		if self.motion_planning.gripper_state('close') == -1:
			#Redo
			return goal, i

		#Going up after picking the object
		self.motion_planning.waypoints(0.07)
				
		#Getting the output location
		quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
		(r,p,y) = euler_from_quaternion(quat, axes='sxyz')

		r,p,y= (r ,1.57079632,0)

		if name == "pudding_box" or name == "potted_meat_can":
			r = r + 1.57079632

		#Calculating difference between centroid and grasping center
		diff_x = obj_pose.pose.position.x - grasp_pose.pose.position.x
		diff_y = obj_pose.pose.position.y - grasp_pose.pose.position.y

		#Getting the Quaternion coordinates from Euler
		goal_list = [goal.pose_list[i].position.x, goal.pose_list[i].position.y, goal.pose_list[i].position.z*2, r, p, y]
		offset_list = [0.0, 0.0, 0.03, 0, 0, 0]
		self.motion_planning.move_arm(pose_rpy = goal_list, offset = offset_list, pose_type = 1)

		#rospy.sleep(5)
		#Going down to place the object
		self.motion_planning.waypoints(-0.03)

		#Opening the gripper
		self.motion_planning.gripper_state('open')

		#Moving up from the placing location
		self.motion_planning.waypoints(0.07)

		#Closing the gripper back
		#self.motion_planning.gripper_state('gripper_close')

		#Going back to task pose
		self.motion_planning.move_arm(pose_type = 2)


		res_im_feedback = self.feedback(goal,i)
		counter = 0
		if (res_im_feedback) == -1: 
			i+=1
			return goal,i
		while (int(res_im_feedback)!=1 and counter < 2):
			res_im_feedback = self.feedback(goal,i)
			counter+=1

		i+=1

		return goal, i
