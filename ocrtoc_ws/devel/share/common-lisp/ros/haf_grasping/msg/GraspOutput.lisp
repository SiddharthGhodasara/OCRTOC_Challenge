; Auto-generated. Do not edit!


(cl:in-package haf_grasping-msg)


;//! \htmlinclude GraspOutput.msg.html

(cl:defclass <GraspOutput> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (eval
    :reader eval
    :initarg :eval
    :type cl:integer
    :initform 0)
   (graspPoint1
    :reader graspPoint1
    :initarg :graspPoint1
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (graspPoint2
    :reader graspPoint2
    :initarg :graspPoint2
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (averagedGraspPoint
    :reader averagedGraspPoint
    :initarg :averagedGraspPoint
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (approachVector
    :reader approachVector
    :initarg :approachVector
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (roll
    :reader roll
    :initarg :roll
    :type cl:float
    :initform 0.0))
)

(cl:defclass GraspOutput (<GraspOutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspOutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspOutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-msg:<GraspOutput> is deprecated: use haf_grasping-msg:GraspOutput instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:header-val is deprecated.  Use haf_grasping-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'eval-val :lambda-list '(m))
(cl:defmethod eval-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:eval-val is deprecated.  Use haf_grasping-msg:eval instead.")
  (eval m))

(cl:ensure-generic-function 'graspPoint1-val :lambda-list '(m))
(cl:defmethod graspPoint1-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:graspPoint1-val is deprecated.  Use haf_grasping-msg:graspPoint1 instead.")
  (graspPoint1 m))

(cl:ensure-generic-function 'graspPoint2-val :lambda-list '(m))
(cl:defmethod graspPoint2-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:graspPoint2-val is deprecated.  Use haf_grasping-msg:graspPoint2 instead.")
  (graspPoint2 m))

(cl:ensure-generic-function 'averagedGraspPoint-val :lambda-list '(m))
(cl:defmethod averagedGraspPoint-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:averagedGraspPoint-val is deprecated.  Use haf_grasping-msg:averagedGraspPoint instead.")
  (averagedGraspPoint m))

(cl:ensure-generic-function 'approachVector-val :lambda-list '(m))
(cl:defmethod approachVector-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:approachVector-val is deprecated.  Use haf_grasping-msg:approachVector instead.")
  (approachVector m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <GraspOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-msg:roll-val is deprecated.  Use haf_grasping-msg:roll instead.")
  (roll m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspOutput>) ostream)
  "Serializes a message object of type '<GraspOutput>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'eval)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'graspPoint1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'graspPoint2) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'averagedGraspPoint) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'approachVector) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'roll))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspOutput>) istream)
  "Deserializes a message object of type '<GraspOutput>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'eval) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'graspPoint1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'graspPoint2) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'averagedGraspPoint) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'approachVector) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'roll) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspOutput>)))
  "Returns string type for a message object of type '<GraspOutput>"
  "haf_grasping/GraspOutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspOutput)))
  "Returns string type for a message object of type 'GraspOutput"
  "haf_grasping/GraspOutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspOutput>)))
  "Returns md5sum for a message object of type '<GraspOutput>"
  "5d81f8c795c680629cc920340e4f0008")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspOutput)))
  "Returns md5sum for a message object of type 'GraspOutput"
  "5d81f8c795c680629cc920340e4f0008")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspOutput>)))
  "Returns full string definition for message of type '<GraspOutput>"
  (cl:format cl:nil "Header header~%int32 eval~%geometry_msgs/Point graspPoint1~%geometry_msgs/Point graspPoint2~%geometry_msgs/Point averagedGraspPoint~%geometry_msgs/Vector3 approachVector~%float32 roll # radians~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspOutput)))
  "Returns full string definition for message of type 'GraspOutput"
  (cl:format cl:nil "Header header~%int32 eval~%geometry_msgs/Point graspPoint1~%geometry_msgs/Point graspPoint2~%geometry_msgs/Point averagedGraspPoint~%geometry_msgs/Vector3 approachVector~%float32 roll # radians~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspOutput>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'graspPoint1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'graspPoint2))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'averagedGraspPoint))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'approachVector))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspOutput>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspOutput
    (cl:cons ':header (header msg))
    (cl:cons ':eval (eval msg))
    (cl:cons ':graspPoint1 (graspPoint1 msg))
    (cl:cons ':graspPoint2 (graspPoint2 msg))
    (cl:cons ':averagedGraspPoint (averagedGraspPoint msg))
    (cl:cons ':approachVector (approachVector msg))
    (cl:cons ':roll (roll msg))
))
