; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude GraspSearchCenter-request.msg.html

(cl:defclass <GraspSearchCenter-request> (roslisp-msg-protocol:ros-message)
  ((graspsearchcenter
    :reader graspsearchcenter
    :initarg :graspsearchcenter
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass GraspSearchCenter-request (<GraspSearchCenter-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspSearchCenter-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspSearchCenter-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspSearchCenter-request> is deprecated: use haf_grasping-srv:GraspSearchCenter-request instead.")))

(cl:ensure-generic-function 'graspsearchcenter-val :lambda-list '(m))
(cl:defmethod graspsearchcenter-val ((m <GraspSearchCenter-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:graspsearchcenter-val is deprecated.  Use haf_grasping-srv:graspsearchcenter instead.")
  (graspsearchcenter m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspSearchCenter-request>) ostream)
  "Serializes a message object of type '<GraspSearchCenter-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'graspsearchcenter) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspSearchCenter-request>) istream)
  "Deserializes a message object of type '<GraspSearchCenter-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'graspsearchcenter) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspSearchCenter-request>)))
  "Returns string type for a service object of type '<GraspSearchCenter-request>"
  "haf_grasping/GraspSearchCenterRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchCenter-request)))
  "Returns string type for a service object of type 'GraspSearchCenter-request"
  "haf_grasping/GraspSearchCenterRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspSearchCenter-request>)))
  "Returns md5sum for a message object of type '<GraspSearchCenter-request>"
  "2e7151a3ec270e58847862555bffd4c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspSearchCenter-request)))
  "Returns md5sum for a message object of type 'GraspSearchCenter-request"
  "2e7151a3ec270e58847862555bffd4c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspSearchCenter-request>)))
  "Returns full string definition for message of type '<GraspSearchCenter-request>"
  (cl:format cl:nil "geometry_msgs/Point graspsearchcenter~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspSearchCenter-request)))
  "Returns full string definition for message of type 'GraspSearchCenter-request"
  (cl:format cl:nil "geometry_msgs/Point graspsearchcenter~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspSearchCenter-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'graspsearchcenter))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspSearchCenter-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspSearchCenter-request
    (cl:cons ':graspsearchcenter (graspsearchcenter msg))
))
;//! \htmlinclude GraspSearchCenter-response.msg.html

(cl:defclass <GraspSearchCenter-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GraspSearchCenter-response (<GraspSearchCenter-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspSearchCenter-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspSearchCenter-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspSearchCenter-response> is deprecated: use haf_grasping-srv:GraspSearchCenter-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GraspSearchCenter-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspSearchCenter-response>) ostream)
  "Serializes a message object of type '<GraspSearchCenter-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspSearchCenter-response>) istream)
  "Deserializes a message object of type '<GraspSearchCenter-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspSearchCenter-response>)))
  "Returns string type for a service object of type '<GraspSearchCenter-response>"
  "haf_grasping/GraspSearchCenterResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchCenter-response)))
  "Returns string type for a service object of type 'GraspSearchCenter-response"
  "haf_grasping/GraspSearchCenterResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspSearchCenter-response>)))
  "Returns md5sum for a message object of type '<GraspSearchCenter-response>"
  "2e7151a3ec270e58847862555bffd4c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspSearchCenter-response)))
  "Returns md5sum for a message object of type 'GraspSearchCenter-response"
  "2e7151a3ec270e58847862555bffd4c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspSearchCenter-response>)))
  "Returns full string definition for message of type '<GraspSearchCenter-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspSearchCenter-response)))
  "Returns full string definition for message of type 'GraspSearchCenter-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspSearchCenter-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspSearchCenter-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspSearchCenter-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GraspSearchCenter)))
  'GraspSearchCenter-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GraspSearchCenter)))
  'GraspSearchCenter-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchCenter)))
  "Returns string type for a service object of type '<GraspSearchCenter>"
  "haf_grasping/GraspSearchCenter")