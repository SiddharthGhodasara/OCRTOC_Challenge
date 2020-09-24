;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspInput)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspInput (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPINPUT")
  (make-package "HAF_GRASPING::GRASPINPUT"))

(in-package "ROS")
;;//! \htmlinclude GraspInput.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass haf_grasping::GraspInput
  :super ros::object
  :slots (_input_pc _goal_frame_id _grasp_area_center _grasp_area_length_x _grasp_area_length_y _max_calculation_time _show_only_best_grasp _threshold_grasp_evaluation _approach_vector _gripper_opening_width ))

(defmethod haf_grasping::GraspInput
  (:init
   (&key
    ((:input_pc __input_pc) (instance sensor_msgs::PointCloud2 :init))
    ((:goal_frame_id __goal_frame_id) "")
    ((:grasp_area_center __grasp_area_center) (instance geometry_msgs::Point :init))
    ((:grasp_area_length_x __grasp_area_length_x) 0.0)
    ((:grasp_area_length_y __grasp_area_length_y) 0.0)
    ((:max_calculation_time __max_calculation_time) (instance ros::time :init))
    ((:show_only_best_grasp __show_only_best_grasp) nil)
    ((:threshold_grasp_evaluation __threshold_grasp_evaluation) 0)
    ((:approach_vector __approach_vector) (instance geometry_msgs::Vector3 :init))
    ((:gripper_opening_width __gripper_opening_width) 0)
    )
   (send-super :init)
   (setq _input_pc __input_pc)
   (setq _goal_frame_id (string __goal_frame_id))
   (setq _grasp_area_center __grasp_area_center)
   (setq _grasp_area_length_x (float __grasp_area_length_x))
   (setq _grasp_area_length_y (float __grasp_area_length_y))
   (setq _max_calculation_time __max_calculation_time)
   (setq _show_only_best_grasp __show_only_best_grasp)
   (setq _threshold_grasp_evaluation (round __threshold_grasp_evaluation))
   (setq _approach_vector __approach_vector)
   (setq _gripper_opening_width (round __gripper_opening_width))
   self)
  (:input_pc
   (&rest __input_pc)
   (if (keywordp (car __input_pc))
       (send* _input_pc __input_pc)
     (progn
       (if __input_pc (setq _input_pc (car __input_pc)))
       _input_pc)))
  (:goal_frame_id
   (&optional __goal_frame_id)
   (if __goal_frame_id (setq _goal_frame_id __goal_frame_id)) _goal_frame_id)
  (:grasp_area_center
   (&rest __grasp_area_center)
   (if (keywordp (car __grasp_area_center))
       (send* _grasp_area_center __grasp_area_center)
     (progn
       (if __grasp_area_center (setq _grasp_area_center (car __grasp_area_center)))
       _grasp_area_center)))
  (:grasp_area_length_x
   (&optional __grasp_area_length_x)
   (if __grasp_area_length_x (setq _grasp_area_length_x __grasp_area_length_x)) _grasp_area_length_x)
  (:grasp_area_length_y
   (&optional __grasp_area_length_y)
   (if __grasp_area_length_y (setq _grasp_area_length_y __grasp_area_length_y)) _grasp_area_length_y)
  (:max_calculation_time
   (&optional __max_calculation_time)
   (if __max_calculation_time (setq _max_calculation_time __max_calculation_time)) _max_calculation_time)
  (:show_only_best_grasp
   (&optional __show_only_best_grasp)
   (if __show_only_best_grasp (setq _show_only_best_grasp __show_only_best_grasp)) _show_only_best_grasp)
  (:threshold_grasp_evaluation
   (&optional __threshold_grasp_evaluation)
   (if __threshold_grasp_evaluation (setq _threshold_grasp_evaluation __threshold_grasp_evaluation)) _threshold_grasp_evaluation)
  (:approach_vector
   (&rest __approach_vector)
   (if (keywordp (car __approach_vector))
       (send* _approach_vector __approach_vector)
     (progn
       (if __approach_vector (setq _approach_vector (car __approach_vector)))
       _approach_vector)))
  (:gripper_opening_width
   (&optional __gripper_opening_width)
   (if __gripper_opening_width (setq _gripper_opening_width __gripper_opening_width)) _gripper_opening_width)
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/PointCloud2 _input_pc
    (send _input_pc :serialization-length)
    ;; string _goal_frame_id
    4 (length _goal_frame_id)
    ;; geometry_msgs/Point _grasp_area_center
    (send _grasp_area_center :serialization-length)
    ;; float32 _grasp_area_length_x
    4
    ;; float32 _grasp_area_length_y
    4
    ;; duration _max_calculation_time
    8
    ;; bool _show_only_best_grasp
    1
    ;; int32 _threshold_grasp_evaluation
    4
    ;; geometry_msgs/Vector3 _approach_vector
    (send _approach_vector :serialization-length)
    ;; int32 _gripper_opening_width
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/PointCloud2 _input_pc
       (send _input_pc :serialize s)
     ;; string _goal_frame_id
       (write-long (length _goal_frame_id) s) (princ _goal_frame_id s)
     ;; geometry_msgs/Point _grasp_area_center
       (send _grasp_area_center :serialize s)
     ;; float32 _grasp_area_length_x
       (sys::poke _grasp_area_length_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _grasp_area_length_y
       (sys::poke _grasp_area_length_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; duration _max_calculation_time
       (write-long (send _max_calculation_time :sec) s) (write-long (send _max_calculation_time :nsec) s)
     ;; bool _show_only_best_grasp
       (if _show_only_best_grasp (write-byte -1 s) (write-byte 0 s))
     ;; int32 _threshold_grasp_evaluation
       (write-long _threshold_grasp_evaluation s)
     ;; geometry_msgs/Vector3 _approach_vector
       (send _approach_vector :serialize s)
     ;; int32 _gripper_opening_width
       (write-long _gripper_opening_width s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/PointCloud2 _input_pc
     (send _input_pc :deserialize buf ptr-) (incf ptr- (send _input_pc :serialization-length))
   ;; string _goal_frame_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _goal_frame_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Point _grasp_area_center
     (send _grasp_area_center :deserialize buf ptr-) (incf ptr- (send _grasp_area_center :serialization-length))
   ;; float32 _grasp_area_length_x
     (setq _grasp_area_length_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _grasp_area_length_y
     (setq _grasp_area_length_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; duration _max_calculation_time
     (send _max_calculation_time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _max_calculation_time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _show_only_best_grasp
     (setq _show_only_best_grasp (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _threshold_grasp_evaluation
     (setq _threshold_grasp_evaluation (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Vector3 _approach_vector
     (send _approach_vector :deserialize buf ptr-) (incf ptr- (send _approach_vector :serialization-length))
   ;; int32 _gripper_opening_width
     (setq _gripper_opening_width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get haf_grasping::GraspInput :md5sum-) "7fc0ab7dae77f5f03563273dd280b0a3")
(setf (get haf_grasping::GraspInput :datatype-) "haf_grasping/GraspInput")
(setf (get haf_grasping::GraspInput :definition-)
      "
#Header header                        	# header for time/frame information
sensor_msgs/PointCloud2 input_pc     	# defines the point cloud on which grasps should be calculated (objects)
string goal_frame_id				 	# the frame_id to which the point cloud should be transformed before grasps are calculated
geometry_msgs/Point grasp_area_center 	# center of the region where grasps are searched
float32 grasp_area_length_x				# defines the length of the rectangle (in x direction (in m)) where grasps are searched (with center grasp_area_center)
float32 grasp_area_length_y				# defines the length of the rectangle (in y direction (in m)) where grasps are searched (with center grasp_area_center)


duration max_calculation_time			# maximal calculation time before grasp result is returned
bool show_only_best_grasp				# If true, only the best grasp is shown in visualization
int32 threshold_grasp_evaluation		# defines the threshold for return_first_grasp_over_th if it is set to true (otherwise it is ignored)

geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed 
int32 gripper_opening_width				# defines the factor (actually 1/factor) that is used for pre-grasp opening gripper width 

#geometry_msgs/Vector3 scale_gripper	# Scale of the gripper in x and y direction if it deviates from a gripper of the size of a huMAN hand


================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the \"fields\" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :haf_grasping/GraspInput "7fc0ab7dae77f5f03563273dd280b0a3")


