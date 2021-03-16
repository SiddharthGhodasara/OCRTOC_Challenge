#!/usr/bin/env python

from gazebo_msgs.srv import SpawnModel
import rospy
import rospkg
from geometry_msgs.msg import *

rospy.init_node('ebot_gazebo',anonymous=True)
#print("******************************************")

rospack = rospkg.RosPack()
#print(rospack.get_path('ebot_gazebo'))
spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)

spawn_model_client(
    model_name='banana',
    model_xml=open('/home/siddharth/backup_18.04/ocrtoc_materials/models/banana/visual_meshes/visual.dae', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(0, 0, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
'''
spawn_model_client(
    model_name='water_glass',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/water_glass/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(10.820000, -1.080000, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)

spawn_model_client(
    model_name='adhesive',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/adhesive/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.330001, -3.880001, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='glue',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/glue/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.290000, -3.613000, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='battery',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/soap2/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.395002, -3.450001, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)

spawn_model_client(
    model_name='FPGA_board',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/soap/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.700000, -2.984000, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)

spawn_model_client(
    model_name='robot_wheels',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/robot_wheels/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.550019, -3.229873, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='eYFi_board',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/eYIFI/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(26.780040, -3.209977, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='battery2',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/soap2/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(5.470000, 4.200000, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='glue2',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/glue/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(5.660000, 4.300000, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
spawn_model_client(
    model_name='adhesive2',
    model_xml=open('/home/kaushik/temp_ws/src/sahayak_bot/ebot_gazebo/models/adhesive/model.sdf', 'r').read(),
    robot_namespace='/foo',
    initial_pose= Pose(position= Point(5.310006, 4.359984, 1.2),orientation=Quaternion(0,0,0,1)),
    reference_frame='world'
)
'''
'''
coke_can: 15.219994 -1.143085
water_glass: 15.480000 -1.240000
'''

