#! /usr/bin/env python

#Importing Libraries
import tf
import sys
import copy
import time
import rospy
import tf2_ros
import actionlib
import numpy as np
import moveit_msgs.msg
import message_filters
import moveit_commander
import tf2_geometry_msgs
import geometry_msgs.msg
from std_msgs.msg import String
import xml.etree.ElementTree as ET
from sensor_msgs import point_cloud2
from std_msgs.msg import Header, Int64
from sensor_msgs.msg import PointCloud2
from gazebo_msgs.msg import ContactsState
from visualization_msgs.msg import MarkerArray
from tf.transformations import quaternion_from_euler
from control_msgs.msg import GripperCommandActionGoal
from geometry_msgs.msg import Point, Pose, PointStamped
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal

moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('select_grasp_new',anonymous=True)

tf_buffer = tf2_ros.Buffer(rospy.Duration(2000.0)) #tf buffer length
tf_listener = tf2_ros.TransformListener(tf_buffer)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm_controller")
group_1 = moveit_commander.MoveGroupCommander("gripper_controller")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path' , moveit_msgs.msg.DisplayTrajectory,queue_size=20)
scale = 1

label_pub = rospy.Publisher('/label', String, queue_size=1)

group.set_named_target("task_pose")
plan = group.go(wait=True)

gripper_cmd_pub = rospy.Publisher(rospy.resolve_name('gripper_controller/gripper_cmd/goal'),GripperCommandActionGoal, queue_size=10)

contact1 = None
contact2 = None
def callback(msg1,msg2):
	global contact1
	global contact2
	contact1= msg1.states
	contact2= msg2.states


sub1 = message_filters.Subscriber('/finger1_contact_sensor_state', ContactsState)
sub2 = message_filters.Subscriber('/finger2_contact_sensor_state', ContactsState)
cb = message_filters.TimeSynchronizer([sub1, sub2], 10)
cb.registerCallback(callback)

#sub = rospy.Subscriber('/finger1_contact_sensor_state', ContactsState, callback)

#Publisher to publish the coordinates

#Getting the path to scene dir
"""
materials_path = rospy.get_param('~materials_dir', '/root/ocrtoc_materials')
scenes_dir = materials_path + '/scenes'
rospy.loginfo("Scenes Dir: " + scenes_dir)
task_path = scenes_dir + "/" + task_name + "/target.world"
rospy.loginfo("Task Path: " + task_path)
"""

task_path = '/home/kaushik/ocrtoc_ws/src/ocrtoc_materials_patch/scenes/1-1/target.world'

#Class for model location
class model:
	#Init Function
	def __init__(self, model_name, model_pose, i):
		self.idx = i
		self.name = model_name
		self.posx = model_pose.position.x
		self.posy = model_pose.position.y
		self.posz = model_pose.position.z
		self.orx = model_pose.orientation.x
		self.ory = model_pose.orientation.y
		self.orz = model_pose.orientation.z
		self.orw = model_pose.orientation.w
		self.curx = 0.0
		self.cury = 0.0
		self.curz = 0.0

#Callback function for getting grasp coordinates
grasps_plots = ""
def callback_plots(msg_plots):
	global grasps_plots
	grasps_plots = msg_plots.data.split(" ")
	print(grasps_plots)

#Function to extract grasp coordinates
def get_grasps_coord():
	#Subscribing to the topic publishing the coordinates of grasp
	grasps_plots_sub = rospy.Subscriber('/haf_grasping/grasp_hypothesis_with_eval', String, callback_plots)
	global grasps_plots
	# Wait for gsps to arrive.
	rate = rospy.Rate(1)
	#Running till we get a suitable grasp
	while not rospy.is_shutdown():
		if grasps_plots != "" :
			if int(grasps_plots[0]) > 60:
				print("satisfied grasp condition")
				print(int(grasps_plots[0]))
				break
		else:
			print("searching again for better grasp")
		rate.sleep()

#Function to execute task
def execute_task(model):
	#Getting the location of the model
	x = model.posx
	y = model.posy
	z = model.posz
	#Getting the model name
	name = model.name
	global label_pub
	rospy.loginfo(type(name))
	while label_pub.get_num_connections() < 1:
		None
	label_pub.publish(str(name))
	rospy.Rate(1).sleep()
	#print(name)
	#yolo = rospy.wait_for_message('/pose', PointStamped)
	#yolo_x = yolo.point.x
	#yolo_y = yolo.point.y
	#print("Gto Yolo")
	#Getting the position of model from input
	"""
	get_current_pose(model)
	global coord_x, coord_y, coord_z, f_id

	#Passing that to haf_grasp and getting the grasping coordinates
	g_pose = PointStamped()
	g_pose.header.frame_id = f_id
	g_pose.point.x = coord_x
	g_pose.point.y = coord_y
	g_pose.point.z = coord_z
	pub.publish(g_pose)
	"""
	#Getting yolo cooridnates
	#Getting the grasp coordinates
	new_grasps = rospy.wait_for_message('/haf_grasping/grasp_hypothesis_with_eval', String)
	get_grasps_coord()
	global grasps_plots
	#Extracting the X Y Z coordintes
	position_x = float(grasps_plots[-4])
	position_y = float(grasps_plots[-3])
	position_z = float(grasps_plots[-2])

	#Difference between grasp and COM
	#diff_x = yolo_x - position_x
	#diff_y = yolo_y - position_y

	#Extracting the roll
	roll = float(grasps_plots[-1])
	print(grasps_plots[-1])
	print(roll)
	r,p,y= (roll - 90 ,90,0)
	#Generating a pose stamped messgae
	grasp_pose = geometry_msgs.msg.PoseStamped()
	grasp_pose.header.frame_id = "/world"

	grasp_pose.pose.position.x = position_x
	grasp_pose.pose.position.y = position_y
	grasp_pose.pose.position.z = position_z + 0.1
	#Converting degrees to radians
	r_rad = (r*3.14159265358979323846)/180
	p_rad = (p*3.14159265358979323846)/180
	y_rad = (y*3.14159265358979323846)/180
	   #print(r1,p1,y1)
	#Getting the Quaternion coordinates from Euler
	q = quaternion_from_euler(r_rad,p_rad,y_rad)

	print "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])

	grasp_pose.pose.orientation.x = q[0]#quat[0] #grasps_plots.orientation.x
	grasp_pose.pose.orientation.y = q[1]#quat[1] #grasps_plots.orientation.y
	grasp_pose.pose.orientation.z = q[2]#quat[2] #grasps_plots.orientation.z
	grasp_pose.pose.orientation.w = q[3]#quat[3] #grasps_plots.orientation.w

	#Moving the arm to desired location
	group.set_planning_time(50)
	group.set_pose_target(grasp_pose)

	plan2 = group.plan()
	group.go(wait=True)
	rospy.sleep(1)

	gripper_cmd = GripperCommandActionGoal()
	gripper_cmd.goal.command.position = 0.04
	gripper_cmd.goal.command.max_effort = 0.0
	gripper_cmd_pub.publish(gripper_cmd)
	rospy.loginfo("Pub gripper_cmd")
	rospy.sleep(1.0)

	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z -= scale * 0.1  
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)

	rospy.sleep(1)

	rate = rospy.Rate(30)

	cmd = 0.039
	global contact
	while not rospy.is_shutdown():
		if len(contact1)>0 and len(contact2)>0:
		   print("contact")
		   break
		gripper_cmd.goal.command.position = cmd
		gripper_cmd.goal.command.max_effort = 0.01
		gripper_cmd_pub.publish(gripper_cmd)
		cmd -= 0.0005
		rate.sleep()

	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z += scale * 0.1  
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)
	#Moving the arm to output location
	grasp_pose.pose.position.x = model.posx# + diff_x
	grasp_pose.pose.position.y = model.posy# + diff_y
	grasp_pose.pose.position.z = model.posz + 0.1
	grasp_pose.pose.orientation.x = 0#q[0]#quat[0] #grasps_plots.orientation.x
	grasp_pose.pose.orientation.y = 0.707#q[1]#quat[1] #grasps_plots.orientation.y
	grasp_pose.pose.orientation.z = 0#q[2]#quat[2] #grasps_plots.orientation.z
	grasp_pose.pose.orientation.w = 0.707#q[3]#quat[3] #grasps_plots.orientation.w

	group.set_planning_time(50)
	group.set_pose_target(grasp_pose)

	plan2 = group.plan()
	group.go(wait=True)
	rospy.sleep(1)
	
	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z -= model.posz * 2
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)
	rospy.sleep(1)

	group_1.set_named_target("gripper_open")
	plan3 = group_1.go(wait=True)
	#gripper_cmd.goal.command.position = 0.04
	#gripper_cmd.goal.command.max_effort = 0.01
	#gripper_cmd_pub.publish(gripper_cmd)
	waypoints = []
	wpose = group.get_current_pose().pose
	wpose.position.z += model.posz * 2 
	waypoints.append(copy.deepcopy(wpose))
	(cartesian_plan, fraction) = group.compute_cartesian_path(waypoints,0.01, 0.0)
	group.execute(cartesian_plan, wait=True)
	rospy.sleep(1)

	group_1.set_named_target("gripper_close")
	plan3 = group_1.go(wait=True)
	group.set_named_target("task_pose")
	plan3 = group.go(wait=True)
	rospy.sleep(10)

	print("YAAAAAAAAHHHHHHHHHH!!!!!!")


#Getting the root of the XML tree
root = ET.parse(task_path).getroot()

i = 0
m = []
#Looping over all the elements and selecting models
for child in root.findall('world/model'):
	#Getting the model nametarget.world
	alias = child.attrib['name']
	#Ignoring the ground and table models
	if alias == "ground_plane" or alias == "table":
		continue
	#alias_list.append(alias)
	for uri in child.findall('link/visual/geometry/mesh/uri'):
		model_path = uri.text
		model_name = (model_path.split('://')[-1]).split('/')[0]
		#goal.object_list.append(model_name)
	for pose in child.findall('pose'):
		#Getting the model pose
		model_pose = Pose()
		var_list = map(float, pose.text.split(' '))
		#Linear Coordinates
		model_pose.position.x = var_list[0]
		model_pose.position.y = var_list[1]
		model_pose.position.z = var_list[2]
		#print(var_list)
		#Converting euler angles to quaternion
		quaternion = tf.transformations.quaternion_from_euler(var_list[3], 90, 0)
		#Rotational Coordinates
		model_pose.orientation.x = quaternion[0]
		model_pose.orientation.y = quaternion[1]
		model_pose.orientation.z = quaternion[2]
		model_pose.orientation.w = quaternion[3]
		#Getting relation
		m.append(model(model_name, model_pose, i))
		i = i+1

m = m[1:] + m[:1]
#Looping over all models
for i in range(len(m)):
	execute_task(m[i])
	'''#Get the objects position
	x = m[i].posx
	y = m[i].posy
	z = m[i].posz

	#Getting camera info
	camera_info = rospy.wait_for_message('/kinect/color/camera_info', CameraInfo)
	#Making Camera Model
	cam_model = PinholeCameraModel()
	cam_model.fromCameraInfo(camera_info)

	#Converting XYZ coordinates to UV coordinates
	(u, v) = cam_model.project3dToPixel((x, y, z))

	#Getting the depth image and checking the depth at that point
	depth = rospy.wait_for_message('/kinect/depth/image_raw', Image)
	depth_img = img.frombytes("F", (depth.width, depth.height), depth.data)
	lookup = depth_img.load()
	d = lookup[u, v]

	#If depth is smaller than threshold, ie location is not free
	if d < thres:
		m = m[1:] + m[:1]
		i = i -1

	#If location is free, execute the task
	else:
		#Executing the task
		print("[INFO] Starting task Execution")
		execute_task(m[i])
		print("[INFO] Task Completed Successfully")
'''
