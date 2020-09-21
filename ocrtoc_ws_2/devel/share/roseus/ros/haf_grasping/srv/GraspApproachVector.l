;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspApproachVector)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspApproachVector (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPAPPROACHVECTOR")
  (make-package "HAF_GRASPING::GRASPAPPROACHVECTOR"))
(unless (find-package "HAF_GRASPING::GRASPAPPROACHVECTORREQUEST")
  (make-package "HAF_GRASPING::GRASPAPPROACHVECTORREQUEST"))
(unless (find-package "HAF_GRASPING::GRASPAPPROACHVECTORRESPONSE")
  (make-package "HAF_GRASPING::GRASPAPPROACHVECTORRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass haf_grasping::GraspApproachVectorRequest
  :super ros::object
  :slots (_approach_vector ))

(defmethod haf_grasping::GraspApproachVectorRequest
  (:init
   (&key
    ((:approach_vector __approach_vector) (instance geometry_msgs::Vector3 :init))
    )
   (send-super :init)
   (setq _approach_vector __approach_vector)
   self)
  (:approach_vector
   (&rest __approach_vector)
   (if (keywordp (car __approach_vector))
       (send* _approach_vector __approach_vector)
     (progn
       (if __approach_vector (setq _approach_vector (car __approach_vector)))
       _approach_vector)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Vector3 _approach_vector
    (send _approach_vector :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Vector3 _approach_vector
       (send _approach_vector :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Vector3 _approach_vector
     (send _approach_vector :deserialize buf ptr-) (incf ptr- (send _approach_vector :serialization-length))
   ;;
   self)
  )

(defclass haf_grasping::GraspApproachVectorResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::GraspApproachVectorResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass haf_grasping::GraspApproachVector
  :super ros::object
  :slots ())

(setf (get haf_grasping::GraspApproachVector :md5sum-) "bf44c4c96f0e3a32358147d8b8f8d0e4")
(setf (get haf_grasping::GraspApproachVector :datatype-) "haf_grasping/GraspApproachVector")
(setf (get haf_grasping::GraspApproachVector :request) haf_grasping::GraspApproachVectorRequest)
(setf (get haf_grasping::GraspApproachVector :response) haf_grasping::GraspApproachVectorResponse)

(defmethod haf_grasping::GraspApproachVectorRequest
  (:response () (instance haf_grasping::GraspApproachVectorResponse :init)))

(setf (get haf_grasping::GraspApproachVectorRequest :md5sum-) "bf44c4c96f0e3a32358147d8b8f8d0e4")
(setf (get haf_grasping::GraspApproachVectorRequest :datatype-) "haf_grasping/GraspApproachVectorRequest")
(setf (get haf_grasping::GraspApproachVectorRequest :definition-)
      "geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed 

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
---
bool result

")

(setf (get haf_grasping::GraspApproachVectorResponse :md5sum-) "bf44c4c96f0e3a32358147d8b8f8d0e4")
(setf (get haf_grasping::GraspApproachVectorResponse :datatype-) "haf_grasping/GraspApproachVectorResponse")
(setf (get haf_grasping::GraspApproachVectorResponse :definition-)
      "geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed 

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
---
bool result

")



(provide :haf_grasping/GraspApproachVector "bf44c4c96f0e3a32358147d8b8f8d0e4")


