#! /usr/bin/env python

#Importing libraries
import tf
import os
import cv2
import sys
import copy
import time
import rospy
import rospkg
import tf2_ros
import math
import actionlib
import numpy as np
import message_filters
import moveit_msgs.msg
import moveit_commander
import tf2_geometry_msgs
from std_msgs.msg import *
from PIL import Image as img
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon
from gazebo_msgs.msg import ContactsState
from image_geometry import PinholeCameraModel
from visualization_msgs.msg import MarkerArray
from control_msgs.msg import GripperCommandActionGoal
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
from geometry_msgs.msg import Point, Pose, PointStamped, PoseStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def check_curr_pose(pose1):
    #Getting the root of the XML tree
    root = ET.parse('/home/kaushik/ocrtoc_materials/scenes/1-11/input.world').getroot()

    #Looping over all the elements and selecting models
    for child in root.findall('world/model'):
        #Getting the model nametarget.world
        alias = child.attrib['name']
        #Ignoring the ground and table models
        if alias == "ground_plane" or alias == "table":
            continue
        #alias_list.append(alias)
        for pose in child.findall('pose'):
            #Getting the model pose
            model_pose = Pose()
            var_list = map(float, pose.text.split(' '))
            #Linear Coordinates
            t_x = abs(pose1.pose.position.x - var_list[0])
            t_y = abs(pose1.pose.position.y - var_list[1])
            t_z = abs(pose1.pose.position.z - var_list[2])
           

            (r1,p1,y1) = euler_from_quaternion([pose1.pose.orientation.x,pose1.pose.orientation.y,pose1.pose.orientation.z, pose1.pose.orientation.w] , axes='sxyz')
            o_r = abs(r1-var_list[3])
            o_p = abs(p1-var_list[4])
            o_y = abs(y1-var_list[5])

            print("Roll only: ", o_r)

            return (t_x, t_y, t_z), (o_r,o_p,o_y)

class do_task:

    #Initializing all varibales, publishers and subscribers
    def __init__(self):

        #Initalising the moveit commander
        moveit_commander.roscpp_initialize(sys.argv)

        #Initalizing varibales used
        self.contact1 = None
        self.contact2 = None
        self.obj_pose = {}
        self.obj_size = {}
        self.grasps_plots = ""
        self.grasps_plots_max = ""
        self.swap_name = None
        self.swap = 0
        self.retry = 0
        #Initialising publishers, moveit controllers and other required things
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        #Moveit Initializtion
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("arm_controller")
        self.group_1 = moveit_commander.MoveGroupCommander("gripper_controller")
        self.rs_state_pub = rospy.Publisher('/realsense_state', Float32, queue_size=10)
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
        
        #Label Publisher
        self.label_pub = rospy.Publisher('/label', PoseStamped, queue_size=1)
        
        #Gripper command publisher
        self.gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)
        
        #Contact Sensors Subscribers
        self.sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
        self.sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
        self.cb = message_filters.TimeSynchronizer([self.sub1, self.sub2], 10)
        self.cb.registerCallback(self.callback)

        #Label Publisher
        self.label1_pub = rospy.Publisher('/label_1', String, queue_size=1)

        #Subscribing to pose from 6d Estimation
        #rospy.Subscriber('/pose', PoseStamped, self.yolo_cb)

        #Getting camera info
        self.camera_info = rospy.wait_for_message('/kinect/color/camera_info', CameraInfo)
        #Making Camera Model
        self.cam_model = PinholeCameraModel()
        self.cam_model.fromCameraInfo(self.camera_info)

        #Going the task pose
        self.group.set_named_target("pose1")
        plan = self.group.go(wait=True)


    #Function related to 6D estimation
    def yolo_cb(self, pose):
        #Extracting the label
        header = pose.header.frame_id
        header_list = header.split(',')
        label = str(header_list[0])
        obj_len = float(header_list[1])
        obj_width = float(header_list[2])
        obj_height = float(header_list[3])

        if label not in self.obj_size.keys():
            self.obj_size[label] = [obj_len, obj_width, obj_height]

        self.obj_pose[label] = pose 

    #Function for YOLO Object Detection
    def yolo(self, required_label):

        print("Entered YOLO")
        while self.label1_pub.get_num_connections < 1:
            None
        self.label1_pub.publish(required_label)
        print("yolo published")

        rospy.sleep(1)

        pose = rospy.wait_for_message('/pose', PoseStamped)
        empty_1 = PoseStamped() 
        if empty_1.pose == pose.pose:
            return None

        print("Received pose")

        self.yolo_cb(pose)

        if required_label not in self.obj_pose.keys():
            return None
        else:
            return self.obj_pose[required_label]

    #Function for getting contact sensors data
    def callback(self, msg1, msg2):
        self.contact1 = msg1.states
        self.contact2 = msg2.states

    def callback_plots(self, msg_plots):
        self.grasps_plots = msg_plots.data.split(" ")

    #Function to extract grasp coordinates
    def get_grasps_coord(self, label):
        #Publishing the label for which we grasps
        req_obj = self.yolo(label)
        if req_obj is not None:
            while self.label_pub.get_num_connections < 1:
                None

            self.label_pub.publish(req_obj)
        
        grasp_buffer = []
        
        #Running till we get a suitable grasp
        while not rospy.is_shutdown():
            #Subscribing to the topic publishing the coordinates of grasp
            grasps_plots = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
            grasps_plots_list = grasps_plots.data.split(" ")
            #Checking if grasp exsists
            if (grasps_plots != "" and grasps_plots_list[0] > 2):
                if int(grasps_plots_list[0]) < 100: #without scaling search area, the threshold was 70
                    grasp_buffer.append(grasps_plots_list)
                    if len(grasp_buffer) >= 5: 
                        last_five_grasp = grasp_buffer[-5:-1]
                        self.grasps_plots_max = max(last_five_grasp)
                        
                        break
                    else:
                        pass
                else:
                    print("satisfied grasp condition")
                    break
            rospy.Rate(1).sleep()

    def feedback(self, goal, i): 

        print("Evaluating feedback")

        name = goal.object_list[i]
        #Sending to YOLO and getting output coordinates
        pose = self.yolo(str(name))
        if (pose == None):
            print("Object not detected by YOLO, skipping", name)
            i+=1
            return 1

        #Extracting pose of current object
        pose_curr_x = pose.pose.position.x
        pose_curr_y = pose.pose.position.y
        pose_curr_z = pose.pose.position.z

        (r1,p1,y1) = euler_from_quaternion([pose.pose.orientation.x,pose.pose.orientation.y,pose.pose.orientation.z, pose.pose.orientation.w] , axes='sxyz')
        (r2,p2,y2) = euler_from_quaternion([goal.pose_list[i].orientation.x,goal.pose_list[i].orientation.y,goal.pose_list[i].orientation.z,goal.pose_list[i].orientation.w], axes='sxyz')
        
        trans_err = (abs(pose_curr_x - goal.pose_list[i].position.x) + abs(pose_curr_y - goal.pose_list[i].position.y) + abs(pose_curr_z - goal.pose_list[i].position.z)) 
        print("Error in translation after placing is: ", trans_err)
       
        print("Error in Orientation is : ", (abs(r2-r1) + abs(p2-p1) + abs(y2-y1)))
        print("Roll only after: ", abs(r2-r1))
        #Checking if threshold is within threshold
     
        if abs(pose_curr_x - goal.pose_list[i].position.x) <= 0.05 and abs(pose_curr_y - goal.pose_list[i].position.y) <= 0.05:

            print("Good Job Translation for {}".format(name))
            return 1
        #If not within the threshold, do that object again
        else:
            print("Bad Job Translation for {}".format(name))
            goal, i = self.task(goal, i, 0)
            return 0

  
    
    def task(self, goal, i, orientation):
        print("Value of orientation is : ", orientation)
        print("type of orientation is : ", type(orientation))
        if (orientation == 1):
            print("Changing orientation")
            print("Changing orientation")
            print("Changing orientation")
            print("Changing orientation")
        tc = i
        #Getting the
        name = str(goal.object_list[tc])
        goal_x = goal.pose_list[tc].position.x
        goal_y = goal.pose_list[tc].position.y

        curr_obj_pose = self.yolo(name)

        c_e_t, c_o_t  = check_curr_pose(curr_obj_pose)
        print("Transalation error with initial pose - {}".format(np.asarray(c_e_t).sum()))
        print("Orientation error with initial pose - {}".format(np.asarray(c_o_t).sum()))

        obj_h = self.obj_size[name][0] * float(goal.scale_list[tc])
        obj_w = self.obj_size[name][1] * float(goal.scale_list[tc])

        goal_x1, goal_y1 = goal_x - obj_w/2, goal_y - obj_h/2
        goal_x2, goal_y2 = goal_x - obj_w/2, goal_y + obj_h/2
        goal_x3, goal_y3 = goal_x + obj_w/2, goal_y - obj_h/2
        goal_x4, goal_y4 = goal_x + obj_w/2, goal_y + obj_h/2

        box_1 = [[goal_x1, goal_y1], [goal_x2, goal_y2], [goal_x4, goal_y4], [goal_x3, goal_y3]]

        poly_1 = Polygon(box_1)

        #Get the cuurent coordinates of all other objects
        for j in range(0, len(goal.object_list)):
            if j == tc: 
                continue
        
            pose = self.yolo(str(goal.object_list[j]))
            
            if (pose == None):
                j+=1
                continue
            #Define the region of cuurent yolo object
            var_list = pose.header.frame_id.split(",")
            label = var_list[0]

            #Length of object
            w = self.obj_size[label][0]
            #Width of object
            h = self.obj_size[label][0]

            x = pose.pose.position.x
            y = pose.pose.position.y

            x1, y1 = x - w/2, y - h/2
            x2, y2 = x - w/2, y + h/2
            x3, y3 = x + w/2, y - h/2
            x4, y4 = x + w/2, y + h/2
            box_2 = [[x1, y1], [x2, y2], [x4, y4], [x3, y3]]
            poly_2 = Polygon(box_2)
            
            self.swap = 0
                #Check for intersection
            if poly_1.intersection(poly_2).area != 0:
 
                if self.swap_name == goal.object_list[tc]:
                    self.swap = 1
                    break
                else:
                    
                    self.swap_name = goal.object_list[j]
                    goal.object_list[tc], goal.object_list[j] = goal.object_list[j],goal.object_list[tc]
                    goal.pose_list[tc].position.x , goal.pose_list[j].position.x = goal.pose_list[j].position.x , goal.pose_list[tc].position.x
                    goal.pose_list[tc].position.y, goal.pose_list[j].position.y = goal.pose_list[j].position.y, goal.pose_list[tc].position.y
                    goal.pose_list[tc].position.z, goal.pose_list[j].position.z = goal.pose_list[j].position.z, goal.pose_list[tc].position.z
                        
                    goal.pose_list[tc].orientation.x , goal.pose_list[j].orientation.x  =goal.pose_list[j].orientation.x , goal.pose_list[tc].orientation.x 
                    goal.pose_list[tc].orientation.y , goal.pose_list[j].orientation.y  =goal.pose_list[j].orientation.y , goal.pose_list[tc].orientation.y
                    goal.pose_list[tc].orientation.z , goal.pose_list[j].orientation.z  =goal.pose_list[j].orientation.z , goal.pose_list[tc].orientation.z
                    goal.pose_list[tc].orientation.w , goal.pose_list[j].orientation.w  =goal.pose_list[j].orientation.w , goal.pose_list[tc].orientation.w
                    return goal,i

        #Failure resistance if object is not resistant 	
        name = goal.object_list[i]
        rospy.loginfo(type(name))
        xy_pose = self.yolo(str(name))
        if (xy_pose == None):
            i+=1
            print("Object not detected by YOLO, skipping", name)
            return goal, i

        # rospy.Rate(1).sleep()
        rs_state = 0
        #Extracting centroid coordiantes from YOLO
        yolo_x = xy_pose.pose.position.x
        yolo_y = xy_pose.pose.position.y
        yolo_z = xy_pose.pose.position.z

        #Generating a pose stamped messgae
        rs_pose = PoseStamped()
        rs_pose.header.frame_id = "/world"
        #Assiging Linear Coordinates
        rs_pose.pose.position.x = yolo_x - 0.06
        rs_pose.pose.position.y = yolo_y 
        rs_pose.pose.position.z = yolo_z + 0.17
        #Converting degrees to radians
        r_rad_rs = 0
        p_rad_rs = math.pi/2
        y_rad_rs = 0
        #Getting the Quaternion coordinates from Euler
        q_rs = quaternion_from_euler(r_rad_rs,p_rad_rs,y_rad_rs)
            
        #Assigning orientation value to pose message
        rs_pose.pose.orientation.x = q_rs[0]#quat[0] #grasps_plots.orientation.x
        rs_pose.pose.orientation.y = q_rs[1]#quat[1] #grasps_plots.orientation.y
        rs_pose.pose.orientation.z = q_rs[2]#quat[2] #grasps_plots.orientation.z
        rs_pose.pose.orientation.w = q_rs[3]#quat[3] #grasps_plots.orientation.w

        #Moving the arm to Picking location
        self.group.set_planning_time(50)
        self.group.set_pose_target(rs_pose)
        plan2 = self.group.plan()
        rs_state = self.group.go(wait=True)
        rospy.sleep(1)
        print("before publishing control message to haf grasping")
        #Sending control message to haf_grasping 
        if (rs_state):
            self.rs_state_pub.publish(1.0)
            print("published control message to haf grasping")

        #Getting the grasp coordinates
        self.get_grasps_coord(str(name))
 
        #Extracting the X Y Z coordintes
        position_x = float(self.grasps_plots_max[-4])
        position_y = float(self.grasps_plots_max[-3])
        position_z = float(self.grasps_plots_max[-2])

        #Calculating difference between centroid and grasping center
        diff_x = yolo_x - position_x
        diff_y = yolo_y - position_y

        #Extracting the roll
        roll = float(self.grasps_plots_max[-1])
        print(self.grasps_plots_max[-1])
        r,p,y= (roll + 90 ,90,0)

        #Generating a pose stamped messgae
        grasp_pose = PoseStamped()
        grasp_pose.header.frame_id = "/world"
        #Assiging Linear Coordinates
        grasp_pose.pose.position.x = position_x
        grasp_pose.pose.position.y = position_y
        grasp_pose.pose.position.z = position_z + 0.03
        #Converting degrees to radians
        r_rad = (r*3.14159265358979323846)/180
        p_rad = (p*3.14159265358979323846)/180
        y_rad = (y*3.14159265358979323846)/180
        #Getting the Quaternion coordinates from Euler
        q = quaternion_from_euler(r_rad,p_rad,y_rad)
        
        #Assigning orientation value to pose message
        grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
        grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
        grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
        grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

        #Moving the arm to Picking location
        self.group.set_planning_time(50)
        self.group.set_pose_target(grasp_pose)
        plan2 = self.group.plan()
        self.group.go(wait=True)
        rospy.sleep(1)

        #Opening the gripper
        gripper_cmd = GripperCommandActionGoal()
        gripper_cmd.goal.command.position = 0.04
        gripper_cmd.goal.command.max_effort = 0.0
        self.gripper_cmd_pub.publish(gripper_cmd)
        rospy.loginfo("Pub gripper_cmd")
        rospy.sleep(1)

        #Going down to pick the object
        waypoints = []
        wpose = self.group.get_current_pose().pose
        wpose.position.z -= 0.030 + 0.015
        waypoints.append(copy.deepcopy(wpose))
        (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        self.group.execute(cartesian_plan, wait=True)
        rospy.sleep(1)

        #Closing the gripper till both contact sensors are touching the obejct
        rate = rospy.Rate(20)
        cmd = 0.039
        closure = -1
        

        #Failure case: The robot doesn't grasp object - go back to task pose to save time 
        while not rospy.is_shutdown():
            #Checking if both grippers are touching
            if len(self.contact1)>0 and len(self.contact2)>0:
                closure = 1
                self.retry = 0
                break


            #Checking if we are not reached the lower closinhg limit
            if cmd > 0.005:
                gripper_cmd.goal.command.position = cmd
                gripper_cmd.goal.command.max_effort = 0.01
                self.gripper_cmd_pub.publish(gripper_cmd)
                cmd -= 0.0005
                rate.sleep()

            #Re do the task if the lower limit is reached
            else:
                closure = 0
                break

         

        if (closure == 0 and self.retry < 3): 

            print("Missed object, going back to pose1 and trying again")
            #Opening the gripper
            self.group_1.set_named_target("gripper_open")
            plan3 = self.group_1.go(wait=True)

            #Moving up from the placing location
            waypoints = []
            wpose = self.group.get_current_pose().pose
            wpose.position.z += position_z + 0.15
            waypoints.append(copy.deepcopy(wpose))
            (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
            self.group.execute(cartesian_plan, wait=True)
            rospy.sleep(1)

            #Closing the gripper back
            self.group_1.set_named_target("gripper_close")
            plan3 = self.group_1.go(wait=True)

            #Going back to pose1
            self.group.set_named_target("pose1")
            plan3 = self.group.go(wait=True)
            self.retry+=1
            return goal, i

        #Going down to pick the object
        waypoints = []
        wpose = self.group.get_current_pose().pose
        wpose.position.z += 0.15
        waypoints.append(copy.deepcopy(wpose))
        (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        self.group.execute(cartesian_plan, wait=True)

        #Check object
        rospy.loginfo(type(name))
        

        #
        if (orientation == 1):

            print("Changing orientation of object: ")
            print("Changing orientation of object: ")
            print("Changing orientation of object: ")
            print("Changing orientation of object: ")
            #Moving up from the placing location
            quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
            (r,p,y) = euler_from_quaternion(quat, axes='sxyz')

            r,p,y= (r ,1.57079632,0)

            if name == "pudding_box" or name == "potted_meat_can" or self.swap == 1:
                r = r + 1.57079632
                   #Getting the Quaternion coordinates from Euler
            q = quaternion_from_euler(r,p,y)
            grasp_pose.header.frame_id = "/world"
            grasp_pose.pose.position.x = self.group.get_current_pose().pose.position.x
            grasp_pose.pose.position.y = self.group.get_current_pose().pose.position.y
            grasp_pose.pose.position.z = self.group.get_current_pose().pose.position.z
            grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
            grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
            grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
            grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w


            #Moving the placing location, but 10cm above it
            self.group.set_planning_time(50)
            self.group.set_pose_target(grasp_pose)
            plan2 = self.group.plan()
            
            ret_group_go = self.group.go(wait=True)
            rospy.sleep(1)

            #Closing the gripper back
            self.group_1.set_named_target("gripper_close")
            plan3 = self.group_1.go(wait=True)
            
            #Going back to task pose
            self.group.set_named_target("pose1")
            plan3 = self.group.go(wait=True)
            rospy.sleep(1)

        else: 
            #Getting the output location
            print("orientation override: ")
            print("orientation override: ")
            print("orientation override: ")
            print("orientation override: ")
            quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
            (r,p,y) = euler_from_quaternion(quat, axes='sxyz')

            r,p,y= (r ,1.57079632,0)

            if name == "pudding_box" or name == "potted_meat_can" or self.swap == 1:
                r = r + 1.57079632

            #Getting the Quaternion coordinates from Euler
            q = quaternion_from_euler(r,p,y)
            grasp_pose.header.frame_id = "/world"
            grasp_pose.pose.position.x = goal.pose_list[i].position.x - diff_x
            grasp_pose.pose.position.y = goal.pose_list[i].position.y + diff_y
            grasp_pose.pose.position.z = position_z + 0.1
            grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
            grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
            grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
            grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

            if self.swap == 1: 
                grasp_pose.pose.position.x = 0.3126
                grasp_pose.pose.position.y = 0

            #Moving the placing location, but 10cm above it
            self.group.set_planning_time(50)
            self.group.set_pose_target(grasp_pose)
            plan2 = self.group.plan()
            
            ret_group_go = self.group.go(wait=True)
            rospy.sleep(1)
            
            #Going down to place the object
            waypoints = []
            wpose = self.group.get_current_pose().pose
            wpose.position.z -= position_z + 0.03
            waypoints.append(copy.deepcopy(wpose))
            (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
            self.group.execute(cartesian_plan, wait=True)
            rospy.sleep(1)
            
            #Opening the gripper
            self.group_1.set_named_target("gripper_open")
            plan3 = self.group_1.go(wait=True)

            #Moving up from the placing location
            waypoints = []
            wpose = self.group.get_current_pose().pose
            wpose.position.z += position_z + 0.1
            waypoints.append(copy.deepcopy(wpose))
            (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
            self.group.execute(cartesian_plan, wait=True)
            rospy.sleep(1)

            #Closing the gripper back
            self.group_1.set_named_target("gripper_close")
            plan3 = self.group_1.go(wait=True)
            
            #Going back to task pose
            self.group.set_named_target("pose1")
            plan3 = self.group.go(wait=True)
            rospy.sleep(1)

            if self.swap != 1: 
                res_im_feedback = self.feedback(goal,i)
                counter = 0
                while (int(res_im_feedback)!=1 and counter < 2):
                    res_im_feedback = self.feedback(goal,i)
                    counter+=1
            i+=1
        
        return goal, i