; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude GraspCalculationTimeMax-request.msg.html

(cl:defclass <GraspCalculationTimeMax-request> (roslisp-msg-protocol:ros-message)
  ((max_calculation_time
    :reader max_calculation_time
    :initarg :max_calculation_time
    :type cl:real
    :initform 0))
)

(cl:defclass GraspCalculationTimeMax-request (<GraspCalculationTimeMax-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspCalculationTimeMax-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspCalculationTimeMax-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspCalculationTimeMax-request> is deprecated: use haf_grasping-srv:GraspCalculationTimeMax-request instead.")))

(cl:ensure-generic-function 'max_calculation_time-val :lambda-list '(m))
(cl:defmethod max_calculation_time-val ((m <GraspCalculationTimeMax-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:max_calculation_time-val is deprecated.  Use haf_grasping-srv:max_calculation_time instead.")
  (max_calculation_time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspCalculationTimeMax-request>) ostream)
  "Serializes a message object of type '<GraspCalculationTimeMax-request>"
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspCalculationTimeMax-request>) istream)
  "Deserializes a message object of type '<GraspCalculationTimeMax-request>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspCalculationTimeMax-request>)))
  "Returns string type for a service object of type '<GraspCalculationTimeMax-request>"
  "haf_grasping/GraspCalculationTimeMaxRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspCalculationTimeMax-request)))
  "Returns string type for a service object of type 'GraspCalculationTimeMax-request"
  "haf_grasping/GraspCalculationTimeMaxRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspCalculationTimeMax-request>)))
  "Returns md5sum for a message object of type '<GraspCalculationTimeMax-request>"
  "fe39c4e255168ec5afaa585fcfbd448f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspCalculationTimeMax-request)))
  "Returns md5sum for a message object of type 'GraspCalculationTimeMax-request"
  "fe39c4e255168ec5afaa585fcfbd448f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspCalculationTimeMax-request>)))
  "Returns full string definition for message of type '<GraspCalculationTimeMax-request>"
  (cl:format cl:nil "duration max_calculation_time			# maximal calculation time before grasp result is returned~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspCalculationTimeMax-request)))
  "Returns full string definition for message of type 'GraspCalculationTimeMax-request"
  (cl:format cl:nil "duration max_calculation_time			# maximal calculation time before grasp result is returned~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspCalculationTimeMax-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspCalculationTimeMax-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspCalculationTimeMax-request
    (cl:cons ':max_calculation_time (max_calculation_time msg))
))
;//! \htmlinclude GraspCalculationTimeMax-response.msg.html

(cl:defclass <GraspCalculationTimeMax-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GraspCalculationTimeMax-response (<GraspCalculationTimeMax-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspCalculationTimeMax-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspCalculationTimeMax-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspCalculationTimeMax-response> is deprecated: use haf_grasping-srv:GraspCalculationTimeMax-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GraspCalculationTimeMax-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspCalculationTimeMax-response>) ostream)
  "Serializes a message object of type '<GraspCalculationTimeMax-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspCalculationTimeMax-response>) istream)
  "Deserializes a message object of type '<GraspCalculationTimeMax-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspCalculationTimeMax-response>)))
  "Returns string type for a service object of type '<GraspCalculationTimeMax-response>"
  "haf_grasping/GraspCalculationTimeMaxResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspCalculationTimeMax-response)))
  "Returns string type for a service object of type 'GraspCalculationTimeMax-response"
  "haf_grasping/GraspCalculationTimeMaxResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspCalculationTimeMax-response>)))
  "Returns md5sum for a message object of type '<GraspCalculationTimeMax-response>"
  "fe39c4e255168ec5afaa585fcfbd448f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspCalculationTimeMax-response)))
  "Returns md5sum for a message object of type 'GraspCalculationTimeMax-response"
  "fe39c4e255168ec5afaa585fcfbd448f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspCalculationTimeMax-response>)))
  "Returns full string definition for message of type '<GraspCalculationTimeMax-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspCalculationTimeMax-response)))
  "Returns full string definition for message of type 'GraspCalculationTimeMax-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspCalculationTimeMax-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspCalculationTimeMax-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspCalculationTimeMax-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GraspCalculationTimeMax)))
  'GraspCalculationTimeMax-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GraspCalculationTimeMax)))
  'GraspCalculationTimeMax-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspCalculationTimeMax)))
  "Returns string type for a service object of type '<GraspCalculationTimeMax>"
  "haf_grasping/GraspCalculationTimeMax")