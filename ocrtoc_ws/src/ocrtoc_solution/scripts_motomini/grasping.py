#! /usr/bin/env python

import math
import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

class Grasping:

    #Init Function
    def __init__(self, max_tries = 5, threshold = 90):
        #Defining the publisher
        self.label_pub = rospy.Publisher('/pose', PoseStamped, queue_size=1)

        #Defining trying limit and threshold
        self.max_tries = max_tries
        self.threshold = threshold

    #Function to extract grasp coordinates
    def get_grasps_coord(self, pose):
        
        #Publishing the label to haf_grasping
        while self.label_pub.get_num_connections < 1:
        	#print("Waiting:")
        	pass
        print("Published")
        self.label_pub.publish(pose)
        
        #Defining list to store the grasps
        self.grasp_buffer = []
        
        rospy.sleep(5)
        start = time.time()
        #Running till we get a suitable grasp
        while not rospy.is_shutdown():

            start1 = time.time()
            #Subscribing to the topic publishing the coordinates of grasp
            grasps_plots = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
            
            
            #Spliting and extracting data
            grasps_plots_list = grasps_plots.data.split(" ")
            
            #Checking if grasp exsists
            if (grasps_plots != "" and grasps_plots_list[0] > 2):

                #Breaking if we get score higher than threshold
                if int(grasps_plots_list[0]) < 90:
                    
                    if abs(float(grasps_plots_list[-4]) - pose.pose.position.x) <= 0.1 and abs(float(grasps_plots_list[-3]) - pose.pose.position.y) <= 0.1:
                        self.grasp_buffer.append(grasps_plots_list)
                        print(len(self.grasp_buffer))
                        print("Time Taken", time.time() - start1)
                        if len(self.grasp_buffer) >= self.max_tries: 
                        	latest_grapss = self.grasp_buffer[-self.max_tries:-1]
                        	self.grasps_plots_max = max(self.grasp_buffer)
                        	print(self.grasps_plots_max[0])
                        	break
                        #self.grasps_plots_max = grasps_plots_list
                        #break
                        else:
                        	pass
                    
                    else:
                        pass

                    #self.grasp_buffer.append(grasps_plots_list)
                    #Waiting for maximum 5 grasps
                    #if len(self.grasp_buffer) >= self.max_tries: 
                    #    latest_grapss = self.grasp_buffer[-self.max_tries:-1]
                    #    self.grasps_plots_max = max(latest_grapss)
                    #    break
                    
                    #else:
                    #    pass
                else:
                    self.grasps_plots_max = grasps_plots_list
                    print("satisfied grasp condition")
                    break
            rospy.Rate(1).sleep()

		
        #Extracting the roll
        roll = float(self.grasps_plots_max[-1])
        print("Total Time", time.time() - start)
        print("Best Roll", roll - 90)
        r_rad, p_rad, y_rad = math.radians(roll - 90), 1.5707, 0.0 #
        r_rad = math.atan(math.tan(r_rad))
        #Getting the Quaternion coordinates from Euler
        quaternions = quaternion_from_euler(r_rad, p_rad, y_rad)

        #Generating a pose stamped messgae
        self.grasp_pose = PoseStamped()
        self.grasp_pose.header.frame_id = "/world"
        
        #Assiging Linear Coordinates
        self.grasp_pose.pose.position.x = pose.pose.position.x  - 0.02#float(self.grasps_plots_max[-4])#
        self.grasp_pose.pose.position.y = pose.pose.position.y	#float(self.grasps_plots_max[-3])#
        self.grasp_pose.pose.position.z = float(self.grasps_plots_max[-2]) + 0.01#pose.pose.position.z*1.8#float(self.grasps_plots_max[-2]) + 0.01#pose.pose.position.z*1.8#$float(self.grasps_plots_max[-2]) + 0.03
        
        
        #Assigning orientation value to pose message
        self.grasp_pose.pose.orientation.x = quaternions[0]
        self.grasp_pose.pose.orientation.y = quaternions[1]
        self.grasp_pose.pose.orientation.z = quaternions[2]
        self.grasp_pose.pose.orientation.w = quaternions[3]
        
        print("Grasping Pose", self.grasp_pose)
        return self.grasp_pose
