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
import os
import tf
import cv2
import math
import time
import rospy
import rospkg
import tf2_ros
import numpy as np
import open3d as o3d
import geometry_msgs.msg
import tf2_geometry_msgs
from PIL import Image as img
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel
import open3d 
import open3d as o3d
import numpy as np
from ctypes import * # convert float to uint32
import message_filters
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import copy
import tf 
import time
from tf.transformations import * 
import math
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import *
import sys
from move_arm_class import move_arm

#Defining the bridge
bridge = CvBridge()

#Declaring the publisher
pub = None
#Defining camera info global varibale
camera_info = None
cam_model = None
#Storing the depth
depth = None

voxel_size = 0.005

#Tranform Listener
tf_listener = None
#Transformations
tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length

#Loading the labels
rospack = rospkg.RosPack()
package_path = rospack.get_path('3D_Pose_Estimation')
labelsPath = os.path.sep.join([package_path, 'yolo', 'obj.names'])
pcd_path = os.path.sep.join([package_path, 'meshes'])
LABELS = open(labelsPath).read().strip().split("\n")

#Derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny_2000.weights"])
configPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny-obj.cfg"])

# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

def transform_frames():
    listener = tf.TransformListener()
    rospy.sleep(2)
    trans1,quat1 =listener.lookupTransform("world","camera_rgb_optical_frame",rospy.Time())

    htm1 = tf.transformations.quaternion_matrix(quat1)

    for i in range(0,3):
        htm1[i][3] = trans1[i]

    return htm1

def preprocess_point_cloud(pcd, voxel_size):
    print(":: Downsample with a voxel size %.3f." % voxel_size)
    pcd_down = pcd.voxel_down_sample(voxel_size)

    radius_normal = voxel_size * 2
    print(":: Estimate normal with search radius %.3f." % radius_normal)
    pcd_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = voxel_size * 5
    print(":: Compute FPFH feature with search radius %.3f." % radius_feature)
    pcd_fpfh = o3d.registration.compute_fpfh_feature(pcd_down, o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return pcd_down, pcd_fpfh

def execute_global_registration(source_down, target_down, source_fpfh,
                                target_fpfh, voxel_size):
    distance_threshold = voxel_size * 1.5
    print(":: RANSAC registration on downsampled point clouds.")
    print("   Since the downsampling voxel size is %.3f," % voxel_size)
    print("   we use a liberal distance threshold %.3f." % distance_threshold)
    result = o3d.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, distance_threshold,
        o3d.registration.TransformationEstimationPointToPoint(False),
        4, [
            o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(
                0.9),
            o3d.registration.CorrespondenceCheckerBasedOnDistance(
                distance_threshold)
        ], o3d.registration.RANSACConvergenceCriteria(4000000, 500))
    return result

def refine_registration(source, target, source_fpfh, target_fpfh, voxel_size, transformation):
    distance_threshold = voxel_size * 0.4
    print(":: Point-to-plane ICP registration is applied on original point")
    print("   clouds to refine the alignment. This time we use a strict")
    print("   distance threshold %.3f." % distance_threshold)
    result = o3d.registration.registration_icp(source, target, distance_threshold,transformation,
        o3d.registration.TransformationEstimationPointToPlane())
    return result

def prepare_dataset(source, target, voxel_size, transform):
    print(":: Load two point clouds and disturb initial pose.")
                     
    #source.transform(transform)
    target.transform(transform)

    #draw_registration_result(source, target, np.identity(4))

    source_down, source_fpfh = preprocess_point_cloud(source, voxel_size)
    target_down, target_fpfh = preprocess_point_cloud(target, voxel_size)
    return source, target, source_down, target_down, source_fpfh, target_fpfh

#Function for converting coordinates to base link frame
def uv_to_xyz(cx, cy):
    #Converting to XYZ coordinates
    (x, y, z) = cam_model.projectPixelTo3dRay((cx, cy))
    #Normalising
    x = x/z
    y = y/z
    z = z/z

    #Getting the depth at given coordinates
    depth = rospy.wait_for_message("/camera/depth_registered/image", Image)
    depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
    lookup = depth_img.load()
    d = lookup[cx, cy]

    #Modifying the coordinates
    x *= d
    y *= d
    z *= d

    #Making Point Stamp Message
    grasp_pose = geometry_msgs.msg.PointStamped()
    grasp_pose.header.frame_id = "camera_rgb_optical_frame"
    point = geometry_msgs.msg.Point()
    grasp_pose.point.x =  x
    grasp_pose.point.y =  y
    grasp_pose.point.z =  z

    #Transforming
    target_frame = "world"
    source_frame = "camera_rgb_optical_frame"
    transform = tf_buffer.lookup_transform(target_frame,
                                           source_frame, #source frame
                                           rospy.Time(0), #get the tf at first available time
                                           rospy.Duration(1.0)) #wait for 1 second

    #Applying the transform
    pose_transformed = tf2_geometry_msgs.do_transform_point(grasp_pose, transform)
    #Returning the transform coordinates
    return pose_transformed

def get_total_transformation_pose(rot_transform, trans_transform, length, width, height, label):
    trans = [trans_transform[0][3], trans_transform[1][3], trans_transform[2][3]]

    rot_mat = np.eye(4)
    rot_mat[:3,:3] = ((rot_transform[0][0], rot_transform[0][1], rot_transform[0][2]),(rot_transform[1][0], rot_transform[1][1], rot_transform[1][2]),(rot_transform[2][0], rot_transform[2][1], rot_transform[2][2]))

    rot = tf.transformations.quaternion_from_matrix(rot_mat)

    pose_6d = geometry_msgs.msg.PoseStamped()
    pose_6d.header.frame_id = str(label) + "," + str(length) + "," + str(width) + "," + str(height)
    pose_6d.pose.position.x = trans[0]
    pose_6d.pose.position.y = trans[1]
    pose_6d.pose.position.z = trans[2]
    pose_6d.pose.orientation.x = rot[0]
    pose_6d.pose.orientation.y = rot[1]
    pose_6d.pose.orientation.z = rot[2]
    pose_6d.pose.orientation.w = rot[3]
    
    return pose_6d

def compute_distance(point1, point2):
    dist = ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5
    return dist

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    #source_temp.paint_uniform_color([1, 0.706, 0])
    #target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


class do_task:

    #Initializing all varibales, publishers and subscribers
    def __init__(self):

        #Initalising the moveit commander
        moveit_commander.roscpp_initialize(sys.argv)

        #Initalizing varibales used
        self.obj_pose = {}
        self.obj_size = {}
        self.grasps_plots = ""
        self.grasps_plots_max = ""
        self.swap_name = ""
        self.cv_img = None

        #Initialising publishers, moveit controllers and other required things
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        #Moveit Initializtion
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("arm")
        #self.group_1 = moveit_commander.MoveGroupCommander("gripper_controller")
        self.rs_state_pub = rospy.Publisher('/realsense_state', Float32, queue_size=10)
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
        
        #Label Publisher
        self.label_pub = rospy.Publisher('/pose', PoseStamped, queue_size=1)
        
        #Gripper command publisher
        #elf.gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)

        #Subscribing to pose from 6d Estimation
        #rospy.Subscriber('/pose', geometry_msgs.msg.PoseStamped, self.yolo_cb)

        #Getting camera info
        self.camera_info = rospy.wait_for_message("/camera/rgb/camera_info", CameraInfo)
        #Setting up Camera Model
        self.cam_model = PinholeCameraModel()
        self.cam_model.fromCameraInfo(self.camera_info)
        global cam_model 
        cam_model = self.cam_model
        #Initialising Transformations
        self.tf_listener = tf2_ros.TransformListener(tf_buffer)

        #Subscribinig to image topic
        self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback_img)

        #Initialzinf yrc
        self.yrc_controller = move_arm()

        #Going the task pose
        self.group.set_named_target("init_pose")
        plan = self.group.go(wait=True)

        self.yrc_controller.arm_go()
        
        self.yrc_controller.gripper_go('o')
        
        


    #Prediction Function
    def prediction(self, image):

        #Getting the image dimensions
        (H, W) = image.shape[:2]

        global focal_length
        global center
        global camera_matrix

        center = (W/2, H/2)
        focal_length = center[0] / np.tan(60/2 * np.pi / 180)
        camera_matrix = np.array([[focal_length, 0, center[0]],
                                [0, focal_length, center[1]],
                                [0, 0, 1]], dtype = "double")

        # determine only the *output* layer names that we need from YOLO
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        #Creating Blob from images
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        
        #Feeding the blob as input
        net.setInput(blob)
        #Forward pass
        layerOutputs = net.forward(ln)

        #Initializing lists of Detected Bounding Boxes, Confidences, and Class IDs
        boxes = []
        confidences = []
        classIDs = []

        #Looping over each of the layer outputs
        for output in layerOutputs:
            #Looping over each of the detections
            for detection in output:
                #Extracting the class ID and confidence
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                #Filtering out weak predictions
                if confidence > 0.5:
                    #Scale the Bounding Box Coordinates
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    # use the center (x, y)-coordinates to derive the top and
                    # and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    #Updating the Lists
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        #Applying non-max Suppression
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

        #Ensuring at least one detection exists
        if len(idxs) > 0:
            #Looping over the indexes
            print(len(idxs))
            for i in idxs.flatten():
                #Extracting the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                #Getting the labels
                label = LABELS[classIDs[i]]

                #nter coordinates
                cx = x + (w/2)
                cy = y + (h/2)

                #Converting the center cooridnates to base link frame
                xy_pose = uv_to_xyz(cx, cy)

                #Comupting Initial Transformation Matrix
                trans_init = np.array([[1.0, 0.0, 0.0, xy_pose.point.x], [0.0, 1.0, 0.0, xy_pose.point.y], [0.0, 0.0, 1.0, xy_pose.point.z], [0.0, 0.0, 0.0, 1.0]])

                #Extracting the bounding box image
                box_img = image[y-10 : y+h+10, x-10 : x+w+10]
                
                #Converting to RGB Color Space
                box_img = cv2.cvtColor(box_img, cv2.COLOR_BGR2RGB)

                #Getting the depth image
                depth = rospy.wait_for_message("/camera/depth_registered/image", Image)
                
                #Converting to cv2 image from sensor_msg image
                try:
                    dpeth_converted = bridge.imgmsg_to_cv2(depth, desired_encoding='passthrough')
                except CvBridgeError, e:
                    print e

                #Converting to np array
                depth_array = np.array(dpeth_converted)

                #Extracting the depth image of the bounding box
                depth_box = depth_array[y-10 : y+h+10, x-10 : x+w+10]

                #Generating open3D RGBD Image
                o3d_rgbd = o3d.geometry.RGBDImage()
                o3d_rgbd_color = o3d.geometry.Image(box_img)
                o3d_rgbd_depth = o3d.geometry.Image(depth_box.astype(np.float32))
                o3d_rgbd.color = o3d_rgbd_color
                o3d_rgbd.depth = o3d_rgbd_depth
                
                #Computing Intrinsic Parameters of Camera
                intrinsic = o3d.camera.PinholeCameraIntrinsic()
                (H, W) = image.shape[:2]
                center_x = 319.5
                center_y = 239.5
                focal_length_y = 525.0
                focal_length_x = 525.0
                intrinsic.set_intrinsics(W, H, focal_length_x, focal_length_y, center_x, center_y)

                #pcd = o3d.geometry.PointCloud()

                #Generating Point Cloud from RGBD Image
                pcd = o3d.geometry.PointCloud.create_from_rgbd_image(o3d_rgbd, intrinsic)

                obj_mesh_path = os.path.sep.join([pcd_path, label + '.ply'])
                
                #Reading the source comprasion file
                s = o3d.io.read_point_cloud(obj_mesh_path)
                
                #Getting the 3D bounding box of the mesh to extract the size
                bounding_box = s.get_axis_aligned_bounding_box()
                points = bounding_box.get_box_points()

                points_array = np.asarray(points)

                length = compute_distance(points_array[0], points_array[1])
                width = compute_distance(points_array[0], points_array[2])
                height = compute_distance(points_array[0], points_array[3])

                #o3d.visualization.draw_geometries([s, bounding_box])

                #Preprcoessing the point clouds
                source, target, source_down, target_down, source_fpfh, target_fpfh = prepare_dataset(s, pcd, voxel_size, transform_frames())

                #Global Registration
                result_ransac = execute_global_registration(source_down, target_down,source_fpfh, target_fpfh,voxel_size)

                #Local Refinement
                result_icp = refine_registration(source_down, target_down, source_fpfh, target_fpfh,voxel_size,result_ransac.transformation)

                #Visualization
                #draw_registration_result(source, target, result_ransac.transformation)
                #draw_registration_result(source, target, result_icp.transformation)
                print(result_ransac.fitness, result_icp.inlier_rmse)
                
                pose = get_total_transformation_pose(result_icp.transformation, trans_init, length, width, height, label)

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
            return 

    def callback_img(self, data):
        try:
            #Converting Sensor Image to cv2 Image
            self.cv_img = bridge.imgmsg_to_cv2(data, 'bgr8')
            
        #Handling exceptions
        except CvBridgeError as e:
            print(e)

    #Function for YOLO Object Detection
    def yolo(self, required_label):
        if (self.cv_img is None): 
            rospy.sleep(1)
            print("Sleeping...")
        pose = self.prediction(self.cv_img)
        
        if required_label not in self.obj_pose.keys():
            return None
        else:
            return self.obj_pose[required_label]


    def callback_plots(self, msg_plots):
        self.grasps_plots = msg_plots.data.split(" ")

    #Function to extract grasp coordinates
    def get_grasps_coord(self, label):
        #Publishing the label for which we grasps
        req_obj = self.yolo(label)
        if req_obj is not None:
            while self.label_pub.get_num_connections < 1:
                None

            print(req_obj)
            self.label_pub.publish(req_obj)
        
        grasp_buffer = []
        
        #Running till we get a suitable grasp
        while not rospy.is_shutdown():
            #Subscribing to the topic publishing the coordinates of grasp
            grasps_plots = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
            grasps_plots_list = grasps_plots.data.split(" ")
            print(grasps_plots_list[-1])
            #Checking if grasp exsists
            if (grasps_plots != "" and grasps_plots_list[0] > 2):
                #self.grasps_plots_max = grasps_plots_list
                #break
                
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
	
	q1 = [pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w]
	q2 = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
        (r1,p1,y1) = euler_from_quaternion(q1, axes='sxyz')
        (r2,p2,y2) = euler_from_quaternion(q2, axes='sxyz')
        print("Error in rpy: ")
        print((r2-r1), (p2-p1), (y2-y1))
        
        #Checking if threshold is within threshold
        if abs(pose_curr_x - goal.pose_list[i].position.x) <= 0.15 and abs(pose_curr_y - goal.pose_list[i].position.y) <= 0.15:

            print("Good Job Translation for {}".format(name))
            if abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x) <= 0.15 and abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y) <= 0.15 and abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z) <= 0.15 and abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w) <= 0.15:
                print("Good Orientation")
                print("Error in x", abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x))
                print("Error in y", abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y))
                print("Error in z", abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z))
                print("Error in w", abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w))
            else:
                print("Error in x", abs(pose.pose.orientation.x -  goal.pose_list[i].orientation.x))
                print("Error in y", abs(pose.pose.orientation.y -  goal.pose_list[i].orientation.y))
                print("Error in z", abs(pose.pose.orientation.z -  goal.pose_list[i].orientation.z))
                print("Error in w", abs(pose.pose.orientation.w -  goal.pose_list[i].orientation.w))
            return 1

        #If not within the threshold, do that object again
        else:
            print("Bad Job Translation for {}".format(name))
            goal, i = self.task(goal, i)
            return 0

    def task(self, goal, i):
	print("Task Started")
        tc = i
        #Getting the
        name = str(goal.object_list[tc])
        goal_x = goal.pose_list[tc].position.x
        goal_y = goal.pose_list[tc].position.y

        while name not in self.obj_size.keys():
            pose = self.yolo(name)
            rospy.sleep(1)

        obj_h = self.obj_size[name][0]
        obj_w = self.obj_size[name][1]

        goal_x1, goal_y1 = goal_x - obj_w/2, goal_y - obj_h/2
        goal_x2, goal_y2 = goal_x - obj_w/2, goal_y + obj_h/2
        goal_x3, goal_y3 = goal_x + obj_w/2, goal_y - obj_h/2
        goal_x4, goal_y4 = goal_x + obj_w/2, goal_y + obj_h/2

        box_1 = [[goal_x1, goal_y1], [goal_x2, goal_y2], [goal_x4, goal_y4], [goal_x3, goal_y3]]

        poly_1 = Polygon(box_1)

        '''#Get the cuurent coordinates of all other objects
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
                    swap = 1
                    break
                else:
                    
                    swap_name = goal.object_list[j]
                    goal.object_list[tc], goal.object_list[j] = goal.object_list[j],goal.object_list[tc]
                    goal.pose_list[tc].position.x , goal.pose_list[j].position.x = goal.pose_list[j].position.x , goal.pose_list[tc].position.x
                    goal.pose_list[tc].position.y, goal.pose_list[j].position.y = goal.pose_list[j].position.y, goal.pose_list[tc].position.y
                    goal.pose_list[tc].position.z, goal.pose_list[j].position.z = goal.pose_list[j].position.z, goal.pose_list[tc].position.z
                        
                    goal.pose_list[tc].orientation.x , goal.pose_list[j].orientation.x  =goal.pose_list[j].orientation.x , goal.pose_list[tc].orientation.x 
                    goal.pose_list[tc].orientation.y , goal.pose_list[j].orientation.y  =goal.pose_list[j].orientation.y , goal.pose_list[tc].orientation.y
                    goal.pose_list[tc].orientation.z , goal.pose_list[j].orientation.z  =goal.pose_list[j].orientation.z , goal.pose_list[tc].orientation.z
                    goal.pose_list[tc].orientation.w , goal.pose_list[j].orientation.w  =goal.pose_list[j].orientation.w , goal.pose_list[tc].orientation.w
                    return goal,i
	'''
        #Failure resistance if object is not resistant 	
        name = goal.object_list[i]
        rospy.loginfo(type(name))
        xy_pose = self.yolo(str(name))
        print("Pose found")
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
        rs_pose.pose.position.x = yolo_x -0.05#- 0.08
        rs_pose.pose.position.y = yolo_y -0.03#- 0.01
        rs_pose.pose.position.z = yolo_z + 0.13
        
        #Converting degrees to radians
        #r_rad_rs = math.atan2(yolo_y, yolo_x)#0#math.atan2(yolo_y, yolo_x) #Roll
        #p_rad_rs = math.pi/2 #Pitch 
        #y_rad_rs = 0#math.atan2(yolo_y, yolo_x)#0#math.pi #Yaw
        #Getting the Quaternion coordinates from Euler
        
        #r_rad_rs = math.atan2(-rs_pose.pose.position.y, rs_pose.pose.position.x)
        r_rad_rs = math.atan2(-yolo_y, yolo_x)
        p_rad_rs = 1.5707
        y_rad_rs = 0.0
        
        
        q_rs = quaternion_from_euler(r_rad_rs,p_rad_rs,y_rad_rs)
       
            
        #Assigning orientation value to pose message
        rs_pose.pose.orientation.x = q_rs[0]#quat[0] #grasps_plots.orientation.x
        rs_pose.pose.orientation.y = q_rs[1]#quat[1] #grasps_plots.orientation.y
        rs_pose.pose.orientation.z = q_rs[2]#quat[2] #grasps_plots.orientation.z
        rs_pose.pose.orientation.w = q_rs[3]#quat[3] #grasps_plots.orientation.w

        #Moving the arm to Picking location
        #print(rs_pose)
        #self.group.set_planning_time(20)
        #self.group.set_pose_target(rs_pose)
        #plan2 = self.group.plan()
        #rs_state = self.group.go(wait=True)
        #xxxxxxx = raw_input("Input")
        #Make the robot move
        #self.yrc_controller.arm_go()
		
		
        #rospy.sleep(1)
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
        print("Best ROll", roll)
        print(self.grasps_plots_max[-1])
        if position_y < 0:
        	r,p,y= (roll - 90, 90, 0)#(0 ,0, roll) #(roll, 90, 0)
	else:
		r,p,y= (roll + 90, 90, 0)
        #Generating a pose stamped messgae
        grasp_pose = PoseStamped()
        grasp_pose.header.frame_id = "/world"
        #Assiging Linear Coordinates
        grasp_pose.pose.position.x = position_x + 0.02
        grasp_pose.pose.position.y = position_y + 0.02
        grasp_pose.pose.position.z = position_z + 0.05
        #Converting degrees to radians
        r_rad = (r*3.14159265358979323846)/180
        p_rad = (p*3.14159265358979323846)/180
        y_rad = (y*3.14159265358979323846)/180
        #Getting the Quaternion coordinates from Euler
        q = quaternion_from_euler(math.atan(math.tan(r_rad)),p_rad,y_rad) #math.atan(math.tan(r_rad) + math.atan2(-position_y, position_x))
        print(math.atan(math.tan(r_rad)))
        #Assigning orientation value to pose message
        grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
        grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
        grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
        grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

        print(grasp_pose)
        #Moving the arm to Picking location
        self.group.set_planning_time(20)
        self.group.set_pose_target(grasp_pose)
        plan2 = self.group.plan()
        self.group.go(wait=True)

        
        #Make the robot move
        self.yrc_controller.arm_go()


        rospy.sleep(1)


        #Opening the gripper
        self.yrc_controller.gripper_go('o')
        #gripper_cmd = GripperCommandActionGoal()
        #gripper_cmd.goal.command.position = 0.04
        #gripper_cmd.goal.command.max_effort = 0.0
        #self.gripper_cmd_pub.publish(gripper_cmd)
        rospy.loginfo("Pub gripper_cmd")
        rospy.sleep(1)

        #Going down to pick the object
        waypoints = []
        wpose = self.group.get_current_pose().pose
        wpose.position.z -=  0.050
        waypoints.append(copy.deepcopy(wpose))
        (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        self.group.execute(cartesian_plan, wait=True)
        
        
        xxxx = raw_input("Input")
        	
        #Make the robot move
        self.yrc_controller.arm_go()
        
        rospy.sleep(1)

        #Closing the gripper
        self.yrc_controller.gripper_go('c')

        #Coming back up after pick object
        waypoints = []
        wpose = self.group.get_current_pose().pose
        wpose.position.z += 0.07
        waypoints.append(copy.deepcopy(wpose))
        (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        self.group.execute(cartesian_plan, wait=True)

        #Make the robot move
        self.yrc_controller.arm_go()

        #Check object
        rospy.loginfo(type(name))
        
        #Getting the output location
        quat = [goal.pose_list[i].orientation.x, goal.pose_list[i].orientation.y, goal.pose_list[i].orientation.z, goal.pose_list[i].orientation.w]
        (r,p,y) = euler_from_quaternion(quat, axes='sxyz')

        r,p,y= (r ,1.57079632,0)

        if name == "pudding_box" or name == "potted_meat_can":#:
            r = r + 1.57079632

        #Getting the Quaternion coordinates from Euler
        q = quaternion_from_euler(r,p,y)
        grasp_pose.header.frame_id = "/world"
        grasp_pose.pose.position.x = goal.pose_list[i].position.x - diff_x
        grasp_pose.pose.position.y = goal.pose_list[i].position.y + diff_y
        grasp_pose.pose.position.z = position_z + 0.07
        grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
        grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
        grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
        grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w
        print(grasp_pose)
        #if swap == 1: 
        #    grasp_pose.pose.position.x = 0.3126
        #    grasp_pose.pose.position.y = 0

        #Moving the placing location, but 10cm above it
        self.group.set_planning_time(20)
        self.group.set_pose_target(grasp_pose)
        plan2 = self.group.plan()
        
        ret_group_go = self.group.go(wait=True)

        #Make the robot move
        self.yrc_controller.arm_go()

        rospy.sleep(5)
        
        #self.yrc_controller.gripper_go('o')

        #Going down to place the object
        waypoints = []
        wpose = self.group.get_current_pose().pose
        wpose.position.z -= 0.05
        waypoints.append(copy.deepcopy(wpose))
        (cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        self.group.execute(cartesian_plan, wait=True)

        #Make the robot move
        self.yrc_controller.arm_go()

        rospy.sleep(1)

        #Opening the gripper
        #Make the robot move
        self.yrc_controller.gripper_go('o')

        #Moving up from the placing location
        #waypoints = []
        #wpose = self.group.get_current_pose().pose
        #wpose.position.z += position_z + 0.1
        #waypoints.append(copy.deepcopy(wpose))
        #(cartesian_plan, fraction) = self.group.compute_cartesian_path(waypoints,0.01, 0.0)
        #self.group.execute(cartesian_plan, wait=True)

        #Make the robot move
        #self.yrc_controller.arm_go()


        rospy.sleep(1)

        
        #Going back to task pose
        self.group.set_named_target("init_pose")
        plan3 = self.group.go(wait=True)

        #Make the robot move
        self.yrc_controller.arm_go()
        
        rospy.sleep(2)

        #if swap != 1: 
        res_im_feedback = self.feedback(goal,i)
        counter = 0
        while (int(res_im_feedback)!=1 and counter < 2):
            res_im_feedback = self.feedback(goal,i)
            counter+=1
        i+=1
        
        return goal, i
