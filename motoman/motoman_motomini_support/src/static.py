#!/usr/bin/env python

import random
from gazebo_msgs.srv import SpawnModel
import rospy
import rospkg
from geometry_msgs.msg import *
import tf
rospy.init_node('ocrtoc_gazebo',anonymous=True)
#print("******************************************")

rospack = rospkg.RosPack()
#print(rospack.get_path('ebot_gazebo'))
spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)

quat = tf.transformations.quaternion_from_euler(0.0, 0.0 ,random.uniform(0.0, 3.14))


spawn_model_client(
    model_name='banana',
    model_xml=open('/home/siddharth/ocrtoc_ws/src/ycb-tools/models/ycb/011_banana/banana.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(random.uniform(-0.11, 0.21),  random.uniform(-0.31, 0.31), 0.15),orientation=Quaternion(quat[0], quat[1], quat[2], quat[3])),
    reference_frame='world'
)

quat = tf.transformations.quaternion_from_euler(0.0, 0.0 ,random.uniform(0.0, 3.14))
spawn_model_client(
    model_name='apple',
    model_xml=open('/home/siddharth/ocrtoc_ws/src/ycb-tools/models/ycb/013_apple/apple.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(random.uniform(-0.11, 0.21),  random.uniform(-0.31, 0.31), 0.15),orientation=Quaternion(quat[0], quat[1], quat[2], quat[3])),
    reference_frame='world'
)

quat = tf.transformations.quaternion_from_euler(0.0, 0.0 ,random.uniform(0.0, 3.14))
spawn_model_client(
    model_name='gelatin_box',
    model_xml=open('/home/siddharth/ocrtoc_ws/src/ycb-tools/models/ycb/009_gelatin_box/gelatin_box.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(random.uniform(-0.11, 0.21),  random.uniform(-0.31, 0.31), 0.15),orientation=Quaternion(quat[0], quat[1], quat[2], quat[3])),
    reference_frame='world'
)

quat = tf.transformations.quaternion_from_euler(0.0, 0.0 ,random.uniform(0.0, 3.14))
spawn_model_client(
    model_name='rubiks_cube',
    model_xml=open('/home/siddharth/ocrtoc_ws/src/ycb-tools/models/ycb/077_rubiks_cube/rubiks_cube.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(random.uniform(-0.11, 0.21),  random.uniform(-0.31, 0.31), 0.15),orientation=Quaternion(quat[0], quat[1], quat[2], quat[3])),
    reference_frame='world'
)

quat = tf.transformations.quaternion_from_euler(0.0, 0.0 ,random.uniform(0.0, 3.14))
spawn_model_client(
    model_name='wood_block',
    model_xml=open('/home/siddharth/ocrtoc_ws/src/ycb-tools/models/ycb/036_wood_block/wood_block.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(random.uniform(-0.11, 0.21),  random.uniform(-0.31, 0.31), 0.15),orientation=Quaternion(quat[0], quat[1], quat[2], quat[3])),
    reference_frame='world'
)


