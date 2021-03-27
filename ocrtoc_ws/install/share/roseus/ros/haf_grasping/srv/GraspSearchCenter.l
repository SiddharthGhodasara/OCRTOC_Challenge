;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspSearchCenter)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspSearchCenter (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPSEARCHCENTER")
  (make-package "HAF_GRASPING::GRASPSEARCHCENTER"))
(unless (find-package "HAF_GRASPING::GRASPSEARCHCENTERREQUEST")
  (make-package "HAF_GRASPING::GRASPSEARCHCENTERREQUEST"))
(unless (find-package "HAF_GRASPING::GRASPSEARCHCENTERRESPONSE")
  (make-package "HAF_GRASPING::GRASPSEARCHCENTERRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass haf_grasping::GraspSearchCenterRequest
  :super ros::object
  :slots (_graspsearchcenter ))

(defmethod haf_grasping::GraspSearchCenterRequest
  (:init
   (&key
    ((:graspsearchcenter __graspsearchcenter) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _graspsearchcenter __graspsearchcenter)
   self)
  (:graspsearchcenter
   (&rest __graspsearchcenter)
   (if (keywordp (car __graspsearchcenter))
       (send* _graspsearchcenter __graspsearchcenter)
     (progn
       (if __graspsearchcenter (setq _graspsearchcenter (car __graspsearchcenter)))
       _graspsearchcenter)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _graspsearchcenter
    (send _graspsearchcenter :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _graspsearchcenter
       (send _graspsearchcenter :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _graspsearchcenter
     (send _graspsearchcenter :deserialize buf ptr-) (incf ptr- (send _graspsearchcenter :serialization-length))
   ;;
   self)
  )

(defclass haf_grasping::GraspSearchCenterResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::GraspSearchCenterResponse
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

(defclass haf_grasping::GraspSearchCenter
  :super ros::object
  :slots ())

(setf (get haf_grasping::GraspSearchCenter :md5sum-) "2e7151a3ec270e58847862555bffd4c4")
(setf (get haf_grasping::GraspSearchCenter :datatype-) "haf_grasping/GraspSearchCenter")
(setf (get haf_grasping::GraspSearchCenter :request) haf_grasping::GraspSearchCenterRequest)
(setf (get haf_grasping::GraspSearchCenter :response) haf_grasping::GraspSearchCenterResponse)

(defmethod haf_grasping::GraspSearchCenterRequest
  (:response () (instance haf_grasping::GraspSearchCenterResponse :init)))

(setf (get haf_grasping::GraspSearchCenterRequest :md5sum-) "2e7151a3ec270e58847862555bffd4c4")
(setf (get haf_grasping::GraspSearchCenterRequest :datatype-) "haf_grasping/GraspSearchCenterRequest")
(setf (get haf_grasping::GraspSearchCenterRequest :definition-)
      "geometry_msgs/Point graspsearchcenter

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
bool result

")

(setf (get haf_grasping::GraspSearchCenterResponse :md5sum-) "2e7151a3ec270e58847862555bffd4c4")
(setf (get haf_grasping::GraspSearchCenterResponse :datatype-) "haf_grasping/GraspSearchCenterResponse")
(setf (get haf_grasping::GraspSearchCenterResponse :definition-)
      "geometry_msgs/Point graspsearchcenter

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
bool result

")



(provide :haf_grasping/GraspSearchCenter "2e7151a3ec270e58847862555bffd4c4")


