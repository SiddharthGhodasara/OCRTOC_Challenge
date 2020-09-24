; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude GraspPreGripperOpeningWidth-request.msg.html

(cl:defclass <GraspPreGripperOpeningWidth-request> (roslisp-msg-protocol:ros-message)
  ((gripper_opening_width
    :reader gripper_opening_width
    :initarg :gripper_opening_width
    :type cl:integer
    :initform 0))
)

(cl:defclass GraspPreGripperOpeningWidth-request (<GraspPreGripperOpeningWidth-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspPreGripperOpeningWidth-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspPreGripperOpeningWidth-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspPreGripperOpeningWidth-request> is deprecated: use haf_grasping-srv:GraspPreGripperOpeningWidth-request instead.")))

(cl:ensure-generic-function 'gripper_opening_width-val :lambda-list '(m))
(cl:defmethod gripper_opening_width-val ((m <GraspPreGripperOpeningWidth-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:gripper_opening_width-val is deprecated.  Use haf_grasping-srv:gripper_opening_width instead.")
  (gripper_opening_width m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspPreGripperOpeningWidth-request>) ostream)
  "Serializes a message object of type '<GraspPreGripperOpeningWidth-request>"
  (cl:let* ((signed (cl:slot-value msg 'gripper_opening_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspPreGripperOpeningWidth-request>) istream)
  "Deserializes a message object of type '<GraspPreGripperOpeningWidth-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gripper_opening_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspPreGripperOpeningWidth-request>)))
  "Returns string type for a service object of type '<GraspPreGripperOpeningWidth-request>"
  "haf_grasping/GraspPreGripperOpeningWidthRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspPreGripperOpeningWidth-request)))
  "Returns string type for a service object of type 'GraspPreGripperOpeningWidth-request"
  "haf_grasping/GraspPreGripperOpeningWidthRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspPreGripperOpeningWidth-request>)))
  "Returns md5sum for a message object of type '<GraspPreGripperOpeningWidth-request>"
  "01233f977ab6b3bc3035826d00041c09")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspPreGripperOpeningWidth-request)))
  "Returns md5sum for a message object of type 'GraspPreGripperOpeningWidth-request"
  "01233f977ab6b3bc3035826d00041c09")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspPreGripperOpeningWidth-request>)))
  "Returns full string definition for message of type '<GraspPreGripperOpeningWidth-request>"
  (cl:format cl:nil "int32 gripper_opening_width			# factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspPreGripperOpeningWidth-request)))
  "Returns full string definition for message of type 'GraspPreGripperOpeningWidth-request"
  (cl:format cl:nil "int32 gripper_opening_width			# factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspPreGripperOpeningWidth-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspPreGripperOpeningWidth-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspPreGripperOpeningWidth-request
    (cl:cons ':gripper_opening_width (gripper_opening_width msg))
))
;//! \htmlinclude GraspPreGripperOpeningWidth-response.msg.html

(cl:defclass <GraspPreGripperOpeningWidth-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GraspPreGripperOpeningWidth-response (<GraspPreGripperOpeningWidth-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspPreGripperOpeningWidth-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspPreGripperOpeningWidth-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<GraspPreGripperOpeningWidth-response> is deprecated: use haf_grasping-srv:GraspPreGripperOpeningWidth-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GraspPreGripperOpeningWidth-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspPreGripperOpeningWidth-response>) ostream)
  "Serializes a message object of type '<GraspPreGripperOpeningWidth-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspPreGripperOpeningWidth-response>) istream)
  "Deserializes a message object of type '<GraspPreGripperOpeningWidth-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspPreGripperOpeningWidth-response>)))
  "Returns string type for a service object of type '<GraspPreGripperOpeningWidth-response>"
  "haf_grasping/GraspPreGripperOpeningWidthResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspPreGripperOpeningWidth-response)))
  "Returns string type for a service object of type 'GraspPreGripperOpeningWidth-response"
  "haf_grasping/GraspPreGripperOpeningWidthResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspPreGripperOpeningWidth-response>)))
  "Returns md5sum for a message object of type '<GraspPreGripperOpeningWidth-response>"
  "01233f977ab6b3bc3035826d00041c09")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspPreGripperOpeningWidth-response)))
  "Returns md5sum for a message object of type 'GraspPreGripperOpeningWidth-response"
  "01233f977ab6b3bc3035826d00041c09")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspPreGripperOpeningWidth-response>)))
  "Returns full string definition for message of type '<GraspPreGripperOpeningWidth-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspPreGripperOpeningWidth-response)))
  "Returns full string definition for message of type 'GraspPreGripperOpeningWidth-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspPreGripperOpeningWidth-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspPreGripperOpeningWidth-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspPreGripperOpeningWidth-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GraspPreGripperOpeningWidth)))
  'GraspPreGripperOpeningWidth-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GraspPreGripperOpeningWidth)))
  'GraspPreGripperOpeningWidth-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspPreGripperOpeningWidth)))
  "Returns string type for a service object of type '<GraspPreGripperOpeningWidth>"
  "haf_grasping/GraspPreGripperOpeningWidth")