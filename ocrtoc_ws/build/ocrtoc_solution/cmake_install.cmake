# Install script for directory: /home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_solution

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_solution/catkin_generated/installspace/ocrtoc_solution.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_solution/cmake" TYPE FILE FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_solution/catkin_generated/installspace/ocrtoc_solutionConfig.cmake"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/ocrtoc_solution/catkin_generated/installspace/ocrtoc_solutionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_solution" TYPE FILE FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_solution/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ocrtoc_solution" TYPE DIRECTORY FILES
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_solution/controller"
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_solution/launch"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ocrtoc_solution" TYPE PROGRAM FILES "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/ocrtoc_solution/scripts/commit_solution.py")
endif()

