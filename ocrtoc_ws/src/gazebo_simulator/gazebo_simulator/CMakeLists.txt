cmake_minimum_required(VERSION 2.8.3)

project(gazebo_simulator)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch models DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
