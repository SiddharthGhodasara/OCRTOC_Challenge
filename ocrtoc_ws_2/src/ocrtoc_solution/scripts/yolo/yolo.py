#! /usr/bin/env python

#Importing Libraries
import os
import tf
import cv2
import time
import rospy
import tf2_ros
import numpy as np
import geometry_msgs.msg
import tf2_geometry_msgs
from PIL import Image as img
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from image_geometry import PinholeCameraModel
import rospkg

#Defining the bridge
bridge = CvBridge()
dictionary = {"masterchef_chef_can": [0.102529, 0.102377, 0.140177],
"potted_meat_can": [0.057684, 0.101515, 0.083543],
"pudding_box" : [0.089631, 0.113077, 0.038256],
"wood_block": [0.206002, 0.089939, 0.090569],"jenga": [0.150000, 0.050000, 0.030000]}

#Defining the publisher
pub = rospy.Publisher('/pose', geometry_msgs.msg.PointStamped, queue_size = 10)

#Defining camera info global varibale
camera_info = None
cam_model = None

#Transformations
tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0)) #tf buffer length

#Loading the labels
rospack = rospkg.RosPack()
package_path = rospack.get_path('ocrtoc_solution')
labelsPath = os.path.sep.join([package_path, 'scripts','yolo', 'yolo-coco', "obj.names"])
LABELS = open(labelsPath).read().strip().split("\n")

#Initialize a list of colors to represent each possible class label
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

#Derive the paths to the YOLO weights and model configuration

weightsPath = os.path.sep.join([package_path, 'scripts','yolo' , 'yolo-coco', "yolov3-tiny-obj_5000.weights"])
configPath = os.path.sep.join([package_path, 'scripts','yolo', 'yolo-coco', "yolov3-tiny-obj.cfg"])

# load our YOLO object detector trained on custom data
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

tf_listener = None
depth = None

#Function for converting coordinates to base link frame
def uv_to_xyz(cx, cy):
    #Converting to XYZ coordinates
    (x, y, z) = cam_model.projectPixelTo3dRay((cx, cy))
    #Normalising
    x = x/z
    y = y/z
    z = z/z

    #Getting the depth at given coordinates
    depth = rospy.wait_for_message('/kinect/depth/image_raw', Image)
    depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
    lookup = depth_img.load()
    d = lookup[cx, cy]

    #Modifying the coordinates
    x *= d
    y *= d
    z *= d

    #Making Point Stamp Message
    grasp_pose = geometry_msgs.msg.PointStamped()
    grasp_pose.header.frame_id = "/kinect_optical_frame"
    point = geometry_msgs.msg.Point()
    grasp_pose.point.x =  x
    grasp_pose.point.y =  y
    grasp_pose.point.z =  z

    #Transforming
    target_frame = "world"
    source_frame = "kinect_optical_frame"
    transform = tf_buffer.lookup_transform(target_frame,
                                           source_frame, #source frame
                                           rospy.Time(0), #get the tf at first available time
                                           rospy.Duration(1.0)) #wait for 1 second

    pose_transformed = tf2_geometry_msgs.do_transform_point(grasp_pose, transform)
    #Returning the transform coordinates
    return pose_transformed

l = ""
def cb(msg):
	global l
	l = msg

#Prediction Function
def prediction(image):
    print("Here")
    #Subscribe to the topic
    l = rospy.wait_for_message('/label', String)
    x = l.data.split(',')
    choice = int(x[1])
    ll = x[0]
    scale = float(x[2])
    print("Got label {}".format(ll))
    #Getting the image dimensions
    (H, W) = image.shape[:2]
    #Cropping the image if choice is 2
    if choice == 2:
        c_x = int(W/2)
        c_y = int(H/2)
        x1 = c_x - 50
        x2 = c_x + 50
        y1 = c_y - 50
        y2 = c_y + 50
        image = image[y1:y2, x1:x2]

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
            print(label)
            print(label, ll)
            if label == ll:
                #Getting center coordinates
                cx = x + (w/2)
                cy = y + (h/2)
                if label in dictionary.keys(): 
                    h = dictionary[label][0] * scale
                    w = dictionary[label][1] * scale
                # draw a bounding box rectangle and label on the image
                #color = [int(c) for c in COLORS[classIDs[i]]]
                #cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                #text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                #cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                #Converting the center cooridnates to base link frame
                xy_pose = uv_to_xyz(cx, cy)
                #Converting the extreme cooridnates to base link frame
                xy_pose_2 = uv_to_xyz(x, y)
                #Calculating width and height in base link frame
               # w = abs(xy_pose.point.x - xy_pose_2.point.x)*2
               # h = abs(xy_pose.point.y - xy_pose_2.point.y)*2
                #Publishing the pose
                xy_pose.header.frame_id = label + " ,"  + str(w) + " ," + str(h)
                pub.publish(xy_pose)
                print("Published")
                #cv2.imshow("Image", image)
                #cv2.waitKey(1)
                #rospy.sleep(1)
            #print(pose_transformed)


#Callbakc Function
def callback(data):
    #Handling exceptions
    try:
        #Converting Sensor Image to cv2 Image
        cv_img = bridge.imgmsg_to_cv2(data, 'bgr8')
        #int_mat = np.ones(cv_img.shape, dtype = "uint8")*60
        #cv_img = cv2.add(cv_img, int_mat)
        #Logging

        #Noting the time
        start = time.time()
        #Calling the prediction function
        prediction(cv_img)
        #Noting the stop time
        end = time.time()
        #Logging the time used
        print("[INFO] Time {}".format(end-start))
        #Publishing the labels and coordinates
        #pub.publish(data)

    except CvBridgeError as e:
        print(e)

#Main Function
def main():
    #Initialising the node
    rospy.init_node("object_detection")
    #Getting camera info
    print("Running")
    camera_info = rospy.wait_for_message('/kinect/color/camera_info', CameraInfo)
    print("GOt Cam")
    #Making Camera Model
    global cam_model
    cam_model = PinholeCameraModel()
    cam_model.fromCameraInfo(camera_info)
    #print(cam_model)
    #Transformation
    global tf_listener
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    #Subscribinig to image topic
    sub = rospy.Subscriber('/kinect/color/image_raw', Image, callback)
    #Updating the master
    rospy.spin()

#Calling the main thread
if __name__ == "__main__":
    main()
