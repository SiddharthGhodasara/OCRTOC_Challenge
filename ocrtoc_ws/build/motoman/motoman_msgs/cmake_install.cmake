# Install script for directory: /home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs/msg" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/msg/DynamicJointPoint.msg"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/msg/DynamicJointsGroup.msg"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/msg/DynamicJointState.msg"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/msg/DynamicJointTrajectory.msg"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/msg/DynamicJointTrajectoryFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs/srv" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/srv/CmdJointTrajectoryEx.srv"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/srv/ReadSingleIO.srv"
    "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/srv/WriteSingleIO.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs/cmake" TYPE FILE FILES "/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/catkin_generated/installspace/motoman_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/kaushik/ocrtoc_ws/devel/include/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/kaushik/ocrtoc_ws/devel/share/roseus/ros/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/kaushik/ocrtoc_ws/devel/share/common-lisp/ros/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/kaushik/ocrtoc_ws/devel/share/gennodejs/ros/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/kaushik/ocrtoc_ws/devel/lib/python2.7/dist-packages/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/kaushik/ocrtoc_ws/devel/lib/python2.7/dist-packages/motoman_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/catkin_generated/installspace/motoman_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs/cmake" TYPE FILE FILES "/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/catkin_generated/installspace/motoman_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs/cmake" TYPE FILE FILES
    "/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/catkin_generated/installspace/motoman_msgsConfig.cmake"
    "/home/kaushik/ocrtoc_ws/build/motoman/motoman_msgs/catkin_generated/installspace/motoman_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_msgs" TYPE FILE FILES "/home/kaushik/ocrtoc_ws/src/motoman/motoman_msgs/package.xml")
endif()

