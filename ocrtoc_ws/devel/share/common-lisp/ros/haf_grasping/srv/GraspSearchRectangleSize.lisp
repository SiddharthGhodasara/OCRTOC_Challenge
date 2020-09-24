; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude GraspSearchRectangleSize-request.msg.html

(cl:defclass <GraspSearchRectangleSize-request> (roslisp-msg-protocol:ros-message)
  ((grasp_search_size_x
    :reader grasp_search_size_x
    :initarg :grasp_search_size_x
    :type cl:integer
    :initform 0)
   (grasp_search_size_y
    :reader grasp_search_size_y
    :initarg :grasp_search_size_y
    :type cl:integer
    :initform 0))
)

(cl:defclass GraspSearchRectangleSize-request (<GraspSearchRectangleSize-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspSearchRectangleSize-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspSearchRectangleSize-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspSearchRectangleSize-request> is deprecated: use haf_grasping-srv:GraspSearchRectangleSize-request instead.")))

(cl:ensure-generic-function 'grasp_search_size_x-val :lambda-list '(m))
(cl:defmethod grasp_search_size_x-val ((m <GraspSearchRectangleSize-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:grasp_search_size_x-val is deprecated.  Use haf_grasping-srv:grasp_search_size_x instead.")
  (grasp_search_size_x m))

(cl:ensure-generic-function 'grasp_search_size_y-val :lambda-list '(m))
(cl:defmethod grasp_search_size_y-val ((m <GraspSearchRectangleSize-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:grasp_search_size_y-val is deprecated.  Use haf_grasping-srv:grasp_search_size_y instead.")
  (grasp_search_size_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspSearchRectangleSize-request>) ostream)
  "Serializes a message object of type '<GraspSearchRectangleSize-request>"
  (cl:let* ((signed (cl:slot-value msg 'grasp_search_size_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'grasp_search_size_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspSearchRectangleSize-request>) istream)
  "Deserializes a message object of type '<GraspSearchRectangleSize-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'grasp_search_size_x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'grasp_search_size_y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspSearchRectangleSize-request>)))
  "Returns string type for a service object of type '<GraspSearchRectangleSize-request>"
  "haf_grasping/GraspSearchRectangleSizeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchRectangleSize-request)))
  "Returns string type for a service object of type 'GraspSearchRectangleSize-request"
  "haf_grasping/GraspSearchRectangleSizeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspSearchRectangleSize-request>)))
  "Returns md5sum for a message object of type '<GraspSearchRectangleSize-request>"
  "10248c1006719d0893af769fe3ad61ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspSearchRectangleSize-request)))
  "Returns md5sum for a message object of type 'GraspSearchRectangleSize-request"
  "10248c1006719d0893af769fe3ad61ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspSearchRectangleSize-request>)))
  "Returns full string definition for message of type '<GraspSearchRectangleSize-request>"
  (cl:format cl:nil "int32 grasp_search_size_x~%int32 grasp_search_size_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspSearchRectangleSize-request)))
  "Returns full string definition for message of type 'GraspSearchRectangleSize-request"
  (cl:format cl:nil "int32 grasp_search_size_x~%int32 grasp_search_size_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspSearchRectangleSize-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspSearchRectangleSize-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspSearchRectangleSize-request
    (cl:cons ':grasp_search_size_x (grasp_search_size_x msg))
    (cl:cons ':grasp_search_size_y (grasp_search_size_y msg))
))
;//! \htmlinclude GraspSearchRectangleSize-response.msg.html

(cl:defclass <GraspSearchRectangleSize-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GraspSearchRectangleSize-response (<GraspSearchRectangleSize-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspSearchRectangleSize-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspSearchRectangleSize-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspSearchRectangleSize-response> is deprecated: use haf_grasping-srv:GraspSearchRectangleSize-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GraspSearchRectangleSize-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspSearchRectangleSize-response>) ostream)
  "Serializes a message object of type '<GraspSearchRectangleSize-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspSearchRectangleSize-response>) istream)
  "Deserializes a message object of type '<GraspSearchRectangleSize-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspSearchRectangleSize-response>)))
  "Returns string type for a service object of type '<GraspSearchRectangleSize-response>"
  "haf_grasping/GraspSearchRectangleSizeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchRectangleSize-response)))
  "Returns string type for a service object of type 'GraspSearchRectangleSize-response"
  "haf_grasping/GraspSearchRectangleSizeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspSearchRectangleSize-response>)))
  "Returns md5sum for a message object of type '<GraspSearchRectangleSize-response>"
  "10248c1006719d0893af769fe3ad61ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspSearchRectangleSize-response)))
  "Returns md5sum for a message object of type 'GraspSearchRectangleSize-response"
  "10248c1006719d0893af769fe3ad61ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspSearchRectangleSize-response>)))
  "Returns full string definition for message of type '<GraspSearchRectangleSize-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspSearchRectangleSize-response)))
  "Returns full string definition for message of type 'GraspSearchRectangleSize-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspSearchRectangleSize-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspSearchRectangleSize-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspSearchRectangleSize-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GraspSearchRectangleSize)))
  'GraspSearchRectangleSize-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GraspSearchRectangleSize)))
  'GraspSearchRectangleSize-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspSearchRectangleSize)))
  "Returns string type for a service object of type '<GraspSearchRectangleSize>"
  "haf_grasping/GraspSearchRectangleSize")