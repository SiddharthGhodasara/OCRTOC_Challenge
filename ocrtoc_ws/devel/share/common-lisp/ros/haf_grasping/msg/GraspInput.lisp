; Auto-generated. Do not edit!


(cl:in-package haf_grasping-msg)


;//! \htmlinclude GraspInput.msg.html

(cl:defclass <GraspInput> (roslisp-msg-protocol:ros-message)
  ((input_pc
    :reader input_pc
    :initarg :input_pc
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2))
   (goal_frame_id
    :reader goal_frame_id
    :initarg :goal_frame_id
    :type cl:string
    :initform "")
   (grasp_area_center
    :reader grasp_area_center
    :initarg :grasp_area_center
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (grasp_area_length_x
    :reader grasp_area_length_x
    :initarg :grasp_area_length_x
    :type cl:float
    :initform 0.0)
   (grasp_area_length_y
    :reader grasp_area_length_y
    :initarg :grasp_area_length_y
    :type cl:float
    :initform 0.0)
   (max_calculation_time
    :reader max_calculation_time
    :initarg :max_calculation_time
    :type cl:real
    :initform 0)
   (show_only_best_grasp
    :reader show_only_best_grasp
    :initarg :show_only_best_grasp
    :type cl:boolean
    :initform cl:nil)
   (threshold_grasp_evaluation
    :reader threshold_grasp_evaluation
    :initarg :threshold_grasp_evaluation
    :type cl:integer
    :initform 0)
   (approach_vector
    :reader approach_vector
    :initarg :approach_vector
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (gripper_opening_width
    :reader gripper_opening_width
    :initarg :gripper_opening_width
    :type cl:integer
    :initform 0))
)

(cl:defclass GraspInput (<GraspInput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspInput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspInput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-msg:<GraspInput> is deprecated: use haf_grasping-msg:GraspInput instead.")))

(cl:ensure-generic-function 'input_pc-val :lambda-list '(m))
(cl:defmethod input_pc-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:input_pc-val is deprecated.  Use haf_grasping-msg:input_pc instead.")
  (input_pc m))

(cl:ensure-generic-function 'goal_frame_id-val :lambda-list '(m))
(cl:defmethod goal_frame_id-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:goal_frame_id-val is deprecated.  Use haf_grasping-msg:goal_frame_id instead.")
  (goal_frame_id m))

(cl:ensure-generic-function 'grasp_area_center-val :lambda-list '(m))
(cl:defmethod grasp_area_center-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:grasp_area_center-val is deprecated.  Use haf_grasping-msg:grasp_area_center instead.")
  (grasp_area_center m))

(cl:ensure-generic-function 'grasp_area_length_x-val :lambda-list '(m))
(cl:defmethod grasp_area_length_x-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:grasp_area_length_x-val is deprecated.  Use haf_grasping-msg:grasp_area_length_x instead.")
  (grasp_area_length_x m))

(cl:ensure-generic-function 'grasp_area_length_y-val :lambda-list '(m))
(cl:defmethod grasp_area_length_y-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:grasp_area_length_y-val is deprecated.  Use haf_grasping-msg:grasp_area_length_y instead.")
  (grasp_area_length_y m))

(cl:ensure-generic-function 'max_calculation_time-val :lambda-list '(m))
(cl:defmethod max_calculation_time-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:max_calculation_time-val is deprecated.  Use haf_grasping-msg:max_calculation_time instead.")
  (max_calculation_time m))

(cl:ensure-generic-function 'show_only_best_grasp-val :lambda-list '(m))
(cl:defmethod show_only_best_grasp-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:show_only_best_grasp-val is deprecated.  Use haf_grasping-msg:show_only_best_grasp instead.")
  (show_only_best_grasp m))

(cl:ensure-generic-function 'threshold_grasp_evaluation-val :lambda-list '(m))
(cl:defmethod threshold_grasp_evaluation-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:threshold_grasp_evaluation-val is deprecated.  Use haf_grasping-msg:threshold_grasp_evaluation instead.")
  (threshold_grasp_evaluation m))

(cl:ensure-generic-function 'approach_vector-val :lambda-list '(m))
(cl:defmethod approach_vector-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:approach_vector-val is deprecated.  Use haf_grasping-msg:approach_vector instead.")
  (approach_vector m))

(cl:ensure-generic-function 'gripper_opening_width-val :lambda-list '(m))
(cl:defmethod gripper_opening_width-val ((m <GraspInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:gripper_opening_width-val is deprecated.  Use haf_grasping-msg:gripper_opening_width instead.")
  (gripper_opening_width m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspInput>) ostream)
  "Serializes a message object of type '<GraspInput>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'input_pc) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_frame_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_frame_id))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grasp_area_center) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'grasp_area_length_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'grasp_area_length_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'max_calculation_time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'max_calculation_time) (cl:floor (cl:slot-value msg 'max_calculation_time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'show_only_best_grasp) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'threshold_grasp_evaluation)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'approach_vector) ostream)
  (cl:let* ((signed (cl:slot-value msg 'gripper_opening_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspInput>) istream)
  "Deserializes a message object of type '<GraspInput>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'input_pc) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_frame_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_frame_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grasp_area_center) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'grasp_area_length_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'grasp_area_length_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'max_calculation_time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:slot-value msg 'show_only_best_grasp) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'threshold_grasp_evaluation) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'approach_vector) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gripper_opening_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspInput>)))
  "Returns string type for a message object of type '<GraspInput>"
  "haf_grasping/GraspInput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspInput)))
  "Returns string type for a message object of type 'GraspInput"
  "haf_grasping/GraspInput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspInput>)))
  "Returns md5sum for a message object of type '<GraspInput>"
  "7fc0ab7dae77f5f03563273dd280b0a3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspInput)))
  "Returns md5sum for a message object of type 'GraspInput"
  "7fc0ab7dae77f5f03563273dd280b0a3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspInput>)))
  "Returns full string definition for message of type '<GraspInput>"
  (cl:format cl:nil "~%#Header header                        	# header for time/frame information~%sensor_msgs/PointCloud2 input_pc     	# defines the point cloud on which grasps should be calculated (objects)~%string goal_frame_id				 	# the frame_id to which the point cloud should be transformed before grasps are calculated~%geometry_msgs/Point grasp_area_center 	# center of the region where grasps are searched~%float32 grasp_area_length_x				# defines the length of the rectangle (in x direction (in m)) where grasps are searched (with center grasp_area_center)~%float32 grasp_area_length_y				# defines the length of the rectangle (in y direction (in m)) where grasps are searched (with center grasp_area_center)~%~%~%duration max_calculation_time			# maximal calculation time before grasp result is returned~%bool show_only_best_grasp				# If true, only the best grasp is shown in visualization~%int32 threshold_grasp_evaluation		# defines the threshold for return_first_grasp_over_th if it is set to true (otherwise it is ignored)~%~%geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed ~%int32 gripper_opening_width				# defines the factor (actually 1/factor) that is used for pre-grasp opening gripper width ~%~%#geometry_msgs/Vector3 scale_gripper	# Scale of the gripper in x and y direction if it deviates from a gripper of the size of a huMAN hand~%~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspInput)))
  "Returns full string definition for message of type 'GraspInput"
  (cl:format cl:nil "~%#Header header                        	# header for time/frame information~%sensor_msgs/PointCloud2 input_pc     	# defines the point cloud on which grasps should be calculated (objects)~%string goal_frame_id				 	# the frame_id to which the point cloud should be transformed before grasps are calculated~%geometry_msgs/Point grasp_area_center 	# center of the region where grasps are searched~%float32 grasp_area_length_x				# defines the length of the rectangle (in x direction (in m)) where grasps are searched (with center grasp_area_center)~%float32 grasp_area_length_y				# defines the length of the rectangle (in y direction (in m)) where grasps are searched (with center grasp_area_center)~%~%~%duration max_calculation_time			# maximal calculation time before grasp result is returned~%bool show_only_best_grasp				# If true, only the best grasp is shown in visualization~%int32 threshold_grasp_evaluation		# defines the threshold for return_first_grasp_over_th if it is set to true (otherwise it is ignored)~%~%geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed ~%int32 gripper_opening_width				# defines the factor (actually 1/factor) that is used for pre-grasp opening gripper width ~%~%#geometry_msgs/Vector3 scale_gripper	# Scale of the gripper in x and y direction if it deviates from a gripper of the size of a huMAN hand~%~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspInput>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'input_pc))
     4 (cl:length (cl:slot-value msg 'goal_frame_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grasp_area_center))
     4
     4
     8
     1
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'approach_vector))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspInput>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspInput
    (cl:cons ':input_pc (input_pc msg))
    (cl:cons ':goal_frame_id (goal_frame_id msg))
    (cl:cons ':grasp_area_center (grasp_area_center msg))
    (cl:cons ':grasp_area_length_x (grasp_area_length_x msg))
    (cl:cons ':grasp_area_length_y (grasp_area_length_y msg))
    (cl:cons ':max_calculation_time (max_calculation_time msg))
    (cl:cons ':show_only_best_grasp (show_only_best_grasp msg))
    (cl:cons ':threshold_grasp_evaluation (threshold_grasp_evaluation msg))
    (cl:cons ':approach_vector (approach_vector msg))
    (cl:cons ':gripper_opening_width (gripper_opening_width msg))
))
