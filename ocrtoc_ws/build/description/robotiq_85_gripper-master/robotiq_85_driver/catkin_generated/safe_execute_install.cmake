execute_process(COMMAND "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
