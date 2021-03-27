#! /usr/bin/env python

#Importing Libraries
import os
import tf
import cv2
import time
import rospy
import rospkg
import tf2_ros
import numpy as np
import geometry_msgs.msg
import tf2_geometry_msgs
from PIL import Image as img
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel
import math

#Getting the parameters from launch file
#print(rospy.get_param_names())
image_topic = rospy.get_param("/image_topic")
camera_topic = rospy.get_param('/camera_topic')
depth_topic = rospy.get_param('/depth_topic')
camera_frame = rospy.get_param('/camera_frame')

#Defining global variables
focal_length = None
center = None
camera_matrix = None
dist_coeffs = np.zeros((4,1))

print("Image topic is", image_topic)

#Defining the bridge
bridge = CvBridge()

#Declaring the publisher
pub = None
#Defining camera info global varibale
camera_info = None
cam_model = None
#Storing the depth
depth = None

#Tranform Listener
tf_listener = None
#Transformations
tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length

#Loading the labels
rospack = rospkg.RosPack()
package_path = rospack.get_path('3D_Pose_Estimation')
labelsPath = os.path.sep.join([package_path, 'yolo', 'obj.names'])
LABELS = open(labelsPath).read().strip().split("\n")

#Derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny-obj_4000.weights"])
configPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny-obj.cfg"])
# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


#Function for converting coordinates to base link frame
def uv_to_xyz(cx, cy):
    #Converting to XYZ coordinates
    (x, y, z) = cam_model.projectPixelTo3dRay((cx, cy))
    #Normalising
    x = x/z
    y = y/z
    z = z/z

    #Getting the depth at given coordinates
    depth = rospy.wait_for_message(depth_topic, Image)
    depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
    lookup = depth_img.load()
    d = lookup[cx, cy]

    #Modifying the coordinates
    x *= d
    y *= d
    z *= d

    #Making Point Stamp Message
    grasp_pose = geometry_msgs.msg.PointStamped()
    grasp_pose.header.frame_id = camera_frame
    point = geometry_msgs.msg.Point()
    grasp_pose.point.x =  x
    grasp_pose.point.y =  y
    grasp_pose.point.z =  z

    #Transforming
    target_frame = "world"
    source_frame = camera_frame
    transform = tf_buffer.lookup_transform(target_frame,
                                           source_frame, #source frame
                                           rospy.Time(0), #get the tf at first available time
                                           rospy.Duration(1.0)) #wait for 1 second

    #Applying the transform
    pose_transformed = tf2_geometry_msgs.do_transform_point(grasp_pose, transform)
    #Returning the transform coordinates
    return pose_transformed


#Prediction Function
def prediction(image):
    #Getting the image dimensions
    (H, W) = image.shape[:2]

    global focal_length
    global center
    global camera_matrix

    focal_length = W
    center = (W/2, H/2)
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
        label_str = ""
    	for i in idxs.flatten():
            #Extracting the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            #Getting the labels
            label = LABELS[classIDs[i]]

            box_img = image[y:y+h, x:x+w]

            gray= cv2.cvtColor(box_img,cv2.COLOR_BGR2GRAY)


            #Getting center coordinates
            cx = x + (w/2)
            cy = y + (h/2)

            #Converting the center cooridnates to base link frame
            xy_pose = uv_to_xyz(cx, cy)

            #Publishing the pose
            world_x = xy_pose.point.x
            world_y = xy_pose.point.y
            world_z = xy_pose.point.z

            #Getting center coordinates
            cx = x + (w/2)
            cy = y + (h/2)

            xy_pose_main = uv_to_xyz(cx, cy)

            #Publishing the pose
            world_x = xy_pose_main.point.x
            world_y = xy_pose_main.point.y
            world_z = xy_pose_main.point.z

            c1x = cx + 50
            c1y = cy

            xy_pose = uv_to_xyz(c1x, c1y)

            #Publishing the pose
            world_x1 = xy_pose.point.x
            world_y1 = xy_pose.point.y
            world_z1 = xy_pose.point.z

            c2x = cx + 50
            c2y = cy - 50

            xy_pose = uv_to_xyz(c2x, c2y)

            #Publishing the pose
            world_x2 = xy_pose.point.x
            world_y2 = xy_pose.point.y
            world_z2 = xy_pose.point.z


            c3x = cx
            c3y = cy + 50

            xy_pose = uv_to_xyz(c3x, c3y)

            #Publishing the pose
            world_x3 = xy_pose.point.x
            world_y3 = xy_pose.point.y
            world_z3 = xy_pose.point.z

            c4x = cx
            c4y = cy - 50

            xy_pose = uv_to_xyz(c4x, c4y)

            #Publishing the pose
            world_x4 = xy_pose.point.x
            world_y4 = xy_pose.point.y
            world_z4 = xy_pose.point.z

            c5x = cx + 20
            c5y = cy - 20

            xy_pose = uv_to_xyz(c5x, c5y)

            #Publishing the pose
            world_x5 = xy_pose.point.x
            world_y5 = xy_pose.point.y
            world_z5 = xy_pose.point.z

            c6x = cx - 20
            c6y = cy + 20

            xy_pose = uv_to_xyz(c6x, c6y)

            #Publishing the pose
            world_x6 = xy_pose.point.x
            world_y6 = xy_pose.point.y
            world_z6 = xy_pose.point.z

            image_points = np.array([(cx, cy), (c1x, c1y), (c2x, c2y), (c3x, c3y), (c4x, c4y), (c5x, c5y), (c6x, c6y)],dtype="double")
            model_points = np.array([(world_x, world_y, world_z), (world_x1, world_y1, world_z1), (world_x2, world_y2, world_z2), (world_x3, world_y3, world_z3), (world_x4, world_y4, world_z4), (world_x5, world_y5, world_z5), (world_x6, world_y6, world_z6)])

            (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.cv2.SOLVEPNP_ITERATIVE)

            pose = geometry_msgs.msg.PoseStamped()
            pose.pose.position.x = translation_vector[0]
            pose.pose.position.y = translation_vector[1]
            pose.pose.position.z = translation_vector[2]

            rmat_1, rmat_2 = cv2.Rodrigues(rotation_vector)

            rot_ros = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]])

            rmat_1 = rmat_1*(rot_ros.T)

            q4 = 0.5 * math.sqrt(1.0 + rmat_1[0][0] + rmat_1[1][1] + rmat_1[2][2])
            t = (1.0 / (4.0 * q4))
            q1 = t * (rmat_1[2][1] - rmat_1[1][2])
            q2 = t * (rmat_1[0][2] - rmat_1[2][0])
            q3 = t * (rmat_1[1][0] - rmat_1[0][1])

            pose.pose.orientation.x= q1
            pose.pose.orientation.y= q2
            pose.pose.orientation.z= q3
            pose.pose.orientation.w= q4
            '''
            #Transforming
            target_frame = "world"
            source_frame = camera_frame
            transform = tf_buffer.lookup_transform(target_frame,
                                                source_frame, #source frame
                                                rospy.Time(0), #get the tf at first available time
                                                rospy.Duration(1.0)) #wait for 1 second

            #Applying the transform
            quat_transformed = tf2_geometry_msgs.do_transform_pose(pose, transform)
            '''
                
            #quat = [quat_transformed.pose.orientation.x,quat_transformed.pose.orientation.y,quat_transformed.pose.orientation.z,quat_transformed.pose.orientation.w]
            quat = [q1,q2,q3,q4]
            print(label)
            (r,p,y) = tf.transformations.euler_from_quaternion(quat, axes='sxyz')
            print(r,p,y)


        #Checking if subscribers are present
        while pub.get_num_connections() < 1:
			None
        #Publishing
        pub.publish(label_str)
        print("Published")


#Image Callback Function
def callback(data):
    try:
        #Converting Sensor Image to cv2 Image
        cv_img = bridge.imgmsg_to_cv2(data, 'bgr8')
        #Calling the prediction function
        prediction(cv_img)
    #Handling exceptions
    except CvBridgeError as e:
        print(e)

#Main Function
def main():
    #Defining global variable usage
    global pub
    global cam_model
    global tf_listener

    #Initialising the node
    rospy.init_node("object_detection")

    #Getting camera info
    camera_info = rospy.wait_for_message(camera_topic, CameraInfo)
    #Setting up Camera Model
    cam_model = PinholeCameraModel()
    cam_model.fromCameraInfo(camera_info)

    #Initialising Transformations
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    #Initialising the publisher
    pub = rospy.Publisher('/pose', String, queue_size = 10)
    #Subscribinig to image topic
    sub = rospy.Subscriber(image_topic, Image, callback)

    #Stopping the node from termination
    rospy.spin()

#Calling the main thread
if __name__ == "__main__":
    main()
