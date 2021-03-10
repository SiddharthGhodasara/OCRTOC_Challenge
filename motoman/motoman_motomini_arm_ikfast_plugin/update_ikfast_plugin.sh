search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=motoman_motomini.srdf
robot_name_in_srdf=motoman_motomini
moveit_config_pkg=motoman_motomini_moveit_config
robot_name=motoman_motomini
planning_group_name=arm
ikfast_plugin_pkg=motoman_motomini_arm_ikfast_plugin
base_link_name=base_link
eef_link_name=tool_tip
ikfast_output_path=/home/siddharth/catkin_ws/src/motoman/motoman_motomini_support/urdf/motoman_motomini_arm_ikfast_plugin/src/motoman_motomini_arm_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
