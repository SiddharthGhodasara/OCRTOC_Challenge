; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude GraspApproachVector-request.msg.html

(cl:defclass <GraspApproachVector-request> (roslisp-msg-protocol:ros-message)
  ((approach_vector
    :reader approach_vector
    :initarg :approach_vector
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass GraspApproachVector-request (<GraspApproachVector-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspApproachVector-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspApproachVector-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspApproachVector-request> is deprecated: use haf_grasping-srv:GraspApproachVector-request instead.")))

(cl:ensure-generic-function 'approach_vector-val :lambda-list '(m))
(cl:defmethod approach_vector-val ((m <GraspApproachVector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:approach_vector-val is deprecated.  Use haf_grasping-srv:approach_vector instead.")
  (approach_vector m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspApproachVector-request>) ostream)
  "Serializes a message object of type '<GraspApproachVector-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'approach_vector) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspApproachVector-request>) istream)
  "Deserializes a message object of type '<GraspApproachVector-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'approach_vector) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspApproachVector-request>)))
  "Returns string type for a service object of type '<GraspApproachVector-request>"
  "haf_grasping/GraspApproachVectorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspApproachVector-request)))
  "Returns string type for a service object of type 'GraspApproachVector-request"
  "haf_grasping/GraspApproachVectorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspApproachVector-request>)))
  "Returns md5sum for a message object of type '<GraspApproachVector-request>"
  "bf44c4c96f0e3a32358147d8b8f8d0e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspApproachVector-request)))
  "Returns md5sum for a message object of type 'GraspApproachVector-request"
  "bf44c4c96f0e3a32358147d8b8f8d0e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspApproachVector-request>)))
  "Returns full string definition for message of type '<GraspApproachVector-request>"
  (cl:format cl:nil "geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed ~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspApproachVector-request)))
  "Returns full string definition for message of type 'GraspApproachVector-request"
  (cl:format cl:nil "geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed ~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspApproachVector-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'approach_vector))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspApproachVector-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspApproachVector-request
    (cl:cons ':approach_vector (approach_vector msg))
))
;//! \htmlinclude GraspApproachVector-response.msg.html

(cl:defclass <GraspApproachVector-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GraspApproachVector-response (<GraspApproachVector-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspApproachVector-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspApproachVector-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspApproachVector-response> is deprecated: use haf_grasping-srv:GraspApproachVector-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GraspApproachVector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspApproachVector-response>) ostream)
  "Serializes a message object of type '<GraspApproachVector-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspApproachVector-response>) istream)
  "Deserializes a message object of type '<GraspApproachVector-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspApproachVector-response>)))
  "Returns string type for a service object of type '<GraspApproachVector-response>"
  "haf_grasping/GraspApproachVectorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspApproachVector-response)))
  "Returns string type for a service object of type 'GraspApproachVector-response"
  "haf_grasping/GraspApproachVectorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspApproachVector-response>)))
  "Returns md5sum for a message object of type '<GraspApproachVector-response>"
  "bf44c4c96f0e3a32358147d8b8f8d0e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspApproachVector-response)))
  "Returns md5sum for a message object of type 'GraspApproachVector-response"
  "bf44c4c96f0e3a32358147d8b8f8d0e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspApproachVector-response>)))
  "Returns full string definition for message of type '<GraspApproachVector-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspApproachVector-response)))
  "Returns full string definition for message of type 'GraspApproachVector-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspApproachVector-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspApproachVector-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspApproachVector-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GraspApproachVector)))
  'GraspApproachVector-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GraspApproachVector)))
  'GraspApproachVector-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspApproachVector)))
  "Returns string type for a service object of type '<GraspApproachVector>"
  "haf_grasping/GraspApproachVector")