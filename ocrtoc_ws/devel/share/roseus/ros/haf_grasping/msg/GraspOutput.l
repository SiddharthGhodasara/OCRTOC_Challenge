;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspOutput)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspOutput (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPOUTPUT")
  (make-package "HAF_GRASPING::GRASPOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude GraspOutput.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass haf_grasping::GraspOutput
  :super ros::object
  :slots (_header _eval _graspPoint1 _graspPoint2 _averagedGraspPoint _approachVector _roll ))

(defmethod haf_grasping::GraspOutput
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:eval __eval) 0)
    ((:graspPoint1 __graspPoint1) (instance geometry_msgs::Point :init))
    ((:graspPoint2 __graspPoint2) (instance geometry_msgs::Point :init))
    ((:averagedGraspPoint __averagedGraspPoint) (instance geometry_msgs::Point :init))
    ((:approachVector __approachVector) (instance geometry_msgs::Vector3 :init))
    ((:roll __roll) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _eval (round __eval))
   (setq _graspPoint1 __graspPoint1)
   (setq _graspPoint2 __graspPoint2)
   (setq _averagedGraspPoint __averagedGraspPoint)
   (setq _approachVector __approachVector)
   (setq _roll (float __roll))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:eval
   (&optional __eval)
   (if __eval (setq _eval __eval)) _eval)
  (:graspPoint1
   (&rest __graspPoint1)
   (if (keywordp (car __graspPoint1))
       (send* _graspPoint1 __graspPoint1)
     (progn
       (if __graspPoint1 (setq _graspPoint1 (car __graspPoint1)))
       _graspPoint1)))
  (:graspPoint2
   (&rest __graspPoint2)
   (if (keywordp (car __graspPoint2))
       (send* _graspPoint2 __graspPoint2)
     (progn
       (if __graspPoint2 (setq _graspPoint2 (car __graspPoint2)))
       _graspPoint2)))
  (:averagedGraspPoint
   (&rest __averagedGraspPoint)
   (if (keywordp (car __averagedGraspPoint))
       (send* _averagedGraspPoint __averagedGraspPoint)
     (progn
       (if __averagedGraspPoint (setq _averagedGraspPoint (car __averagedGraspPoint)))
       _averagedGraspPoint)))
  (:approachVector
   (&rest __approachVector)
   (if (keywordp (car __approachVector))
       (send* _approachVector __approachVector)
     (progn
       (if __approachVector (setq _approachVector (car __approachVector)))
       _approachVector)))
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _eval
    4
    ;; geometry_msgs/Point _graspPoint1
    (send _graspPoint1 :serialization-length)
    ;; geometry_msgs/Point _graspPoint2
    (send _graspPoint2 :serialization-length)
    ;; geometry_msgs/Point _averagedGraspPoint
    (send _averagedGraspPoint :serialization-length)
    ;; geometry_msgs/Vector3 _approachVector
    (send _approachVector :serialization-length)
    ;; float32 _roll
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _eval
       (write-long _eval s)
     ;; geometry_msgs/Point _graspPoint1
       (send _graspPoint1 :serialize s)
     ;; geometry_msgs/Point _graspPoint2
       (send _graspPoint2 :serialize s)
     ;; geometry_msgs/Point _averagedGraspPoint
       (send _averagedGraspPoint :serialize s)
     ;; geometry_msgs/Vector3 _approachVector
       (send _approachVector :serialize s)
     ;; float32 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _eval
     (setq _eval (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Point _graspPoint1
     (send _graspPoint1 :deserialize buf ptr-) (incf ptr- (send _graspPoint1 :serialization-length))
   ;; geometry_msgs/Point _graspPoint2
     (send _graspPoint2 :deserialize buf ptr-) (incf ptr- (send _graspPoint2 :serialization-length))
   ;; geometry_msgs/Point _averagedGraspPoint
     (send _averagedGraspPoint :deserialize buf ptr-) (incf ptr- (send _averagedGraspPoint :serialization-length))
   ;; geometry_msgs/Vector3 _approachVector
     (send _approachVector :deserialize buf ptr-) (incf ptr- (send _approachVector :serialization-length))
   ;; float32 _roll
     (setq _roll (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get haf_grasping::GraspOutput :md5sum-) "5d81f8c795c680629cc920340e4f0008")
(setf (get haf_grasping::GraspOutput :datatype-) "haf_grasping/GraspOutput")
(setf (get haf_grasping::GraspOutput :definition-)
      "Header header
int32 eval
geometry_msgs/Point graspPoint1
geometry_msgs/Point graspPoint2
geometry_msgs/Point averagedGraspPoint
geometry_msgs/Vector3 approachVector
float32 roll # radians

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



(provide :haf_grasping/GraspOutput "5d81f8c795c680629cc920340e4f0008")


