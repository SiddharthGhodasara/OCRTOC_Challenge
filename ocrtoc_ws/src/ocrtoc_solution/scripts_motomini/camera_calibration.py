#! /usr/bin/env python

#Importing Libraries
import os
import tf
import cv2
import math
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

#Getting the parameters from launch file
#print(rospy.get_param_names())

#Defining global variables
focal_length = None
center = None
camera_matrix = None
dist_coeffs = np.zeros((4,1))

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
weightsPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny-obj_best.weights"])
configPath = os.path.sep.join([package_path, 'yolo', "yolov3-tiny-obj.cfg"])

# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


#Prediction Function
def prediction(image):
    #Getting the image dimensions
    (H, W) = image.shape[:2]

    focal_length = W
    center = (W/2, H/2)
    camera_matrix = np.array([[525.0, 0, 319.5],
                            [0, 525.0, 239.5],
                            [0, 0, 1]], dtype = "double")
                            
    print(camera_matrix)

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
            
            print(label)
            #Segmenting to get the mask
            box_img = image[y-10 : y+h+10, x-10 : x+w+10]

            
            #Getting center coordinates
            cx = x + (w/2)
            cy = y + (h/2)
            
            if label == 'rubiks_cube':
            
            	cx_rc = cx
            	cy_rc = cy 
            			
            		
            elif label == 'wood_block':
            	
            	cx_wb = cx
            	cy_wb = cy
            	
            elif label == 'gelatin_box':
            
            	cx_gb = cx
            	cy_gb = cy
            	
            elif label == 'apple':
            	cx_a = cx
            	cy_a = cy

            
        image_points = np.array([(cx_rc, cy_rc), (cx_wb, cy_wb), (cx_gb, cy_gb), (cx_a, cy_a)],dtype="double")
        model_points = np.array([(-0.06, -0.20, 0.02867), (0.144, -0.144, 0.0226292), (0.142001, 0.0, 0.01516), (-0.06, 0.20, 0.02867)])

        (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.cv2.SOLVEPNP_ITERATIVE)

        rmat_1, rmat_2 = cv2.Rodrigues(rotation_vector)
        
        
        #translation_vector = (-rmat_1.T) * translation_vector
	
        #rot_ros = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]])

        #rmat_1 = rmat_1*(rot_ros.T)
        
        print("Translation -> {}".format(translation_vector))
        print("Rotation -> {}".format(rmat_1))
        
        cameraPosition = -np.matrix(rmat_1).T * np.matrix(translation_vector)
        
        print(cameraPosition)



#Image Callback Function
def callback(data):
    try:
        #Converting Sensor Image to cv2 Image
        cv_img = bridge.imgmsg_to_cv2(data, 'bgr8')
        #Calling the prediction function
        prediction(cv_img)
        exit
    #Handling exceptions
    except CvBridgeError as e:
        print(e)

#Main Function
def main():
    #Defining global variable usage
    global tf_listener

    #Initialising the node
    rospy.init_node("object_detection")

    #Initialising Transformations
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    #Subscribinig to image topic
    sub = rospy.Subscriber('/camera/rgb/image_raw', Image, callback)

    #Stopping the node from termination
    rospy.spin()

#Calling the main thread
if __name__ == "__main__":
    main()
