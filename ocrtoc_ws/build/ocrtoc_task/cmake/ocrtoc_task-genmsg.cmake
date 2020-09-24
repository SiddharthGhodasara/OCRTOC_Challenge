# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ocrtoc_task: 7 messages, 0 services")

set(MSG_I_FLAGS "-Iocrtoc_task:/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ocrtoc_task_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" ""
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:ocrtoc_task/CleanResult:std_msgs/Header"
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:ocrtoc_task/CleanFeedback:std_msgs/Header"
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" "geometry_msgs/Pose:geometry_msgs/Quaternion:geometry_msgs/Point"
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" ""
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" "actionlib_msgs/GoalID:ocrtoc_task/CleanActionFeedback:ocrtoc_task/CleanResult:actionlib_msgs/GoalStatus:ocrtoc_task/CleanFeedback:ocrtoc_task/CleanActionGoal:ocrtoc_task/CleanGoal:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Quaternion:ocrtoc_task/CleanActionResult:geometry_msgs/Point"
)

get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_custom_target(_ocrtoc_task_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ocrtoc_task" "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" "actionlib_msgs/GoalID:ocrtoc_task/CleanGoal:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_cpp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
)

### Generating Services

### Generating Module File
_generate_module_cpp(ocrtoc_task
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ocrtoc_task_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ocrtoc_task_generate_messages ocrtoc_task_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_cpp _ocrtoc_task_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ocrtoc_task_gencpp)
add_dependencies(ocrtoc_task_gencpp ocrtoc_task_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ocrtoc_task_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_eus(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
)

### Generating Services

### Generating Module File
_generate_module_eus(ocrtoc_task
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ocrtoc_task_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ocrtoc_task_generate_messages ocrtoc_task_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_eus _ocrtoc_task_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ocrtoc_task_geneus)
add_dependencies(ocrtoc_task_geneus ocrtoc_task_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ocrtoc_task_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_lisp(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
)

### Generating Services

### Generating Module File
_generate_module_lisp(ocrtoc_task
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ocrtoc_task_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ocrtoc_task_generate_messages ocrtoc_task_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_lisp _ocrtoc_task_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ocrtoc_task_genlisp)
add_dependencies(ocrtoc_task_genlisp ocrtoc_task_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ocrtoc_task_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_nodejs(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ocrtoc_task
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ocrtoc_task_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ocrtoc_task_generate_messages ocrtoc_task_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_nodejs _ocrtoc_task_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ocrtoc_task_gennodejs)
add_dependencies(ocrtoc_task_gennodejs ocrtoc_task_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ocrtoc_task_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)
_generate_msg_py(ocrtoc_task
  "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
)

### Generating Services

### Generating Module File
_generate_module_py(ocrtoc_task
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ocrtoc_task_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ocrtoc_task_generate_messages ocrtoc_task_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionResult.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanFeedback.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanAction.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/devel/share/ocrtoc_task/msg/CleanActionGoal.msg" NAME_WE)
add_dependencies(ocrtoc_task_generate_messages_py _ocrtoc_task_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ocrtoc_task_genpy)
add_dependencies(ocrtoc_task_genpy ocrtoc_task_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ocrtoc_task_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ocrtoc_task
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(ocrtoc_task_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(ocrtoc_task_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ocrtoc_task_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ocrtoc_task
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(ocrtoc_task_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(ocrtoc_task_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ocrtoc_task_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ocrtoc_task
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(ocrtoc_task_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(ocrtoc_task_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ocrtoc_task_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ocrtoc_task
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(ocrtoc_task_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(ocrtoc_task_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ocrtoc_task_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ocrtoc_task
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(ocrtoc_task_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(ocrtoc_task_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ocrtoc_task_generate_messages_py std_msgs_generate_messages_py)
endif()
