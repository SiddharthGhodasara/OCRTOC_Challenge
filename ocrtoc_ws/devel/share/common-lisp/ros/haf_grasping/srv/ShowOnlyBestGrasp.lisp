; Auto-generated. Do not edit!


(cl:in-package haf_grasping-srv)


;//! \htmlinclude ShowOnlyBestGrasp-request.msg.html

(cl:defclass <ShowOnlyBestGrasp-request> (roslisp-msg-protocol:ros-message)
  ((show_only_best_grasp
    :reader show_only_best_grasp
    :initarg :show_only_best_grasp
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ShowOnlyBestGrasp-request (<ShowOnlyBestGrasp-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ShowOnlyBestGrasp-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ShowOnlyBestGrasp-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<ShowOnlyBestGrasp-request> is deprecated: use haf_grasping-srv:ShowOnlyBestGrasp-request instead.")))

(cl:ensure-generic-function 'show_only_best_grasp-val :lambda-list '(m))
(cl:defmethod show_only_best_grasp-val ((m <ShowOnlyBestGrasp-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:show_only_best_grasp-val is deprecated.  Use haf_grasping-srv:show_only_best_grasp instead.")
  (show_only_best_grasp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ShowOnlyBestGrasp-request>) ostream)
  "Serializes a message object of type '<ShowOnlyBestGrasp-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'show_only_best_grasp) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ShowOnlyBestGrasp-request>) istream)
  "Deserializes a message object of type '<ShowOnlyBestGrasp-request>"
    (cl:setf (cl:slot-value msg 'show_only_best_grasp) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ShowOnlyBestGrasp-request>)))
  "Returns string type for a service object of type '<ShowOnlyBestGrasp-request>"
  "haf_grasping/ShowOnlyBestGraspRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShowOnlyBestGrasp-request)))
  "Returns string type for a service object of type 'ShowOnlyBestGrasp-request"
  "haf_grasping/ShowOnlyBestGraspRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ShowOnlyBestGrasp-request>)))
  "Returns md5sum for a message object of type '<ShowOnlyBestGrasp-request>"
  "c13d71448b4276a64c7f5417c0cd390a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ShowOnlyBestGrasp-request)))
  "Returns md5sum for a message object of type 'ShowOnlyBestGrasp-request"
  "c13d71448b4276a64c7f5417c0cd390a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ShowOnlyBestGrasp-request>)))
  "Returns full string definition for message of type '<ShowOnlyBestGrasp-request>"
  (cl:format cl:nil "bool show_only_best_grasp			# ShowOnlyBestGrasp: defines if only the best grasp should be visualized~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ShowOnlyBestGrasp-request)))
  "Returns full string definition for message of type 'ShowOnlyBestGrasp-request"
  (cl:format cl:nil "bool show_only_best_grasp			# ShowOnlyBestGrasp: defines if only the best grasp should be visualized~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ShowOnlyBestGrasp-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ShowOnlyBestGrasp-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ShowOnlyBestGrasp-request
    (cl:cons ':show_only_best_grasp (show_only_best_grasp msg))
))
;//! \htmlinclude ShowOnlyBestGrasp-response.msg.html

(cl:defclass <ShowOnlyBestGrasp-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ShowOnlyBestGrasp-response (<ShowOnlyBestGrasp-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ShowOnlyBestGrasp-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ShowOnlyBestGrasp-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name haf_grasping-srv:<ShowOnlyBestGrasp-response> is deprecated: use haf_grasping-srv:ShowOnlyBestGrasp-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <ShowOnlyBestGrasp-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader haf_grasping-srv:result-val is deprecated.  Use haf_grasping-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ShowOnlyBestGrasp-response>) ostream)
  "Serializes a message object of type '<ShowOnlyBestGrasp-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ShowOnlyBestGrasp-response>) istream)
  "Deserializes a message object of type '<ShowOnlyBestGrasp-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ShowOnlyBestGrasp-response>)))
  "Returns string type for a service object of type '<ShowOnlyBestGrasp-response>"
  "haf_grasping/ShowOnlyBestGraspResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShowOnlyBestGrasp-response)))
  "Returns string type for a service object of type 'ShowOnlyBestGrasp-response"
  "haf_grasping/ShowOnlyBestGraspResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ShowOnlyBestGrasp-response>)))
  "Returns md5sum for a message object of type '<ShowOnlyBestGrasp-response>"
  "c13d71448b4276a64c7f5417c0cd390a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ShowOnlyBestGrasp-response)))
  "Returns md5sum for a message object of type 'ShowOnlyBestGrasp-response"
  "c13d71448b4276a64c7f5417c0cd390a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ShowOnlyBestGrasp-response>)))
  "Returns full string definition for message of type '<ShowOnlyBestGrasp-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ShowOnlyBestGrasp-response)))
  "Returns full string definition for message of type 'ShowOnlyBestGrasp-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ShowOnlyBestGrasp-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ShowOnlyBestGrasp-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ShowOnlyBestGrasp-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ShowOnlyBestGrasp)))
  'ShowOnlyBestGrasp-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ShowOnlyBestGrasp)))
  'ShowOnlyBestGrasp-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShowOnlyBestGrasp)))
  "Returns string type for a service object of type '<ShowOnlyBestGrasp>"
  "haf_grasping/ShowOnlyBestGrasp")