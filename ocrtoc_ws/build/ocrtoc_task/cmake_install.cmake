# Install script for directory: /home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task/action" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/action/Clean.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task/msg" TYPE FILE FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task/cmake" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_task/catkin_generated/installspace/ocrtoc_task-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/include/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/roseus/ros/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/common-lisp/ros/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/gennodejs/ros/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/lib/python2.7/dist-packages/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/lib/python2.7/dist-packages/ocrtoc_task")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_task/catkin_generated/installspace/ocrtoc_task.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task/cmake" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_task/catkin_generated/installspace/ocrtoc_task-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task/cmake" TYPE FILE FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_task/catkin_generated/installspace/ocrtoc_taskConfig.cmake"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_task/catkin_generated/installspace/ocrtoc_taskConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_task" TYPE DIRECTORY FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/action"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/launch"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/urdf"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ocrtoc_task" TYPE PROGRAM FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/scripts/task_evaluation.pyc"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_task/scripts/trigger_and_evaluation.py"
    )
endif()

