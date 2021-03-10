#!/usr/bin/env python

#Importing Libraries
import rospy
from sensor_msgs.msg import JointState

# Because of transformations
import tf
import tf_conversions
import tf2_ros
import geometry_msgs.msg
from tf.transformations import euler_from_quaternion

rospy.init_node('move_arm_node')

M_PI = 3.14
br = tf2_ros.TransformBroadcaster()
t = geometry_msgs.msg.TransformStamped()

pub = rospy.Publisher('joint_states', JointState, queue_size=1)

t.header.frame_id = "base_link"
t.child_frame_id = 'link_1_s'

joint_state = JointState()


s = 0.47
while not rospy.is_shutdown():
	joint_state.header.stamp = rospy.Time.now();
	joint_state.name = ['joint_1_s', 'joint_2_l', 'joint_3_u', 'joint_4_r', 'joint_5_b', 'joint_6_t']
	#joint_state.position = [0.47, -0.49, 0.50, 0.0, 1.61, -3.61]
	s=s+0.05
	joint_state.position = [s, -0.49, 0.50, 0.0, 1.61, -3.61]
	
	t.header.stamp = rospy.Time.now();
	x, y, z, w = tf.transformations.quaternion_from_euler(0, 0, s, axes='sxyz')
	t.transform.translation.x = 0#cos(angle)*2
	t.transform.translation.y = 0#sin(angle)*2
	t.transform.translation.z = 0#.7
	t.transform.rotation.x = x #tf.createQuaternionMsgFromYaw(s + M_PI/2)
	t.transform.rotation.y = y
	t.transform.rotation.z = z
	t.transform.rotation.w = w
  
  
	print("Done")
	pub.publish(joint_state)
	br.sendTransform(t)
	rospy.Rate(30).sleep()
