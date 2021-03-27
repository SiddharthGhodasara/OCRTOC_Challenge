# Install script for directory: /home/kaushik/ocrtoc_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/kaushik/ocrtoc_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE PROGRAM FILES "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE PROGRAM FILES "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/setup.bash;/home/kaushik/ocrtoc_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/setup.bash"
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/setup.sh;/home/kaushik/ocrtoc_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/setup.sh"
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/setup.zsh;/home/kaushik/ocrtoc_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kaushik/ocrtoc_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kaushik/ocrtoc_ws/install" TYPE FILE FILES "/home/kaushik/ocrtoc_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/kaushik/ocrtoc_ws/build/gtest/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sda10f_moveit_config/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia20d_moveit_config/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_2f_85_gripper_visualization/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_driver/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_simulation/robotiq_85_gazebo/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_gripper/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_simulation/robotiq_85_simulation/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_rqt/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/realsense2_description/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/sapien_simulator/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/ur_e_description/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/3D_Pose_Estimation/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo_simulator/gazebo_simulator/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp12_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp180_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp25_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp50_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp7_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp88_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_gp8_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_hc10_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_hc20_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_mh12_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_mh50_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_mh5_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_motomini_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sda10f_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia10d_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia10f_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia20d_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia50_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_sia5d_support/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_bringup/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_description/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_dispatch_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_knowledge_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_dependencies/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_sensing_interface/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/si_utils/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/ocrtoc_task/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/general-message-pkgs/path_navigation_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_planning_system/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/general-message-pkgs/object_msgs/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo-pkgs/gazebo_test_tools/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo-pkgs/gazebo_version_helpers/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo-pkgs/gazebo_grasp_plugin/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo-pkgs/gazebo_world_plugin_loader/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/general-message-pkgs/object_msgs_tools/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo-pkgs/gazebo_state_plugins/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/haf_grasping/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/ocrtoc_solution/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo_simulator/realsense_plugin/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/gazebo_simulator/roboticsgroup_gazebo_plugins/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_knowledge_base/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/motoman/motoman_driver/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/ur5e_arm_controller_ikfast_plugin/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_moveit_config/cmake_install.cmake")
  include("/home/kaushik/ocrtoc_ws/build/ur5e_moveit_config/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/kaushik/ocrtoc_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
