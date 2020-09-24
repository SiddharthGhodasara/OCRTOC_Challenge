;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspSearchRectangleSize)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspSearchRectangleSize (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZE")
  (make-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZE"))
(unless (find-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZEREQUEST")
  (make-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZEREQUEST"))
(unless (find-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZERESPONSE")
  (make-package "HAF_GRASPING::GRASPSEARCHRECTANGLESIZERESPONSE"))

(in-package "ROS")





(defclass haf_grasping::GraspSearchRectangleSizeRequest
  :super ros::object
  :slots (_grasp_search_size_x _grasp_search_size_y ))

(defmethod haf_grasping::GraspSearchRectangleSizeRequest
  (:init
   (&key
    ((:grasp_search_size_x __grasp_search_size_x) 0)
    ((:grasp_search_size_y __grasp_search_size_y) 0)
    )
   (send-super :init)
   (setq _grasp_search_size_x (round __grasp_search_size_x))
   (setq _grasp_search_size_y (round __grasp_search_size_y))
   self)
  (:grasp_search_size_x
   (&optional __grasp_search_size_x)
   (if __grasp_search_size_x (setq _grasp_search_size_x __grasp_search_size_x)) _grasp_search_size_x)
  (:grasp_search_size_y
   (&optional __grasp_search_size_y)
   (if __grasp_search_size_y (setq _grasp_search_size_y __grasp_search_size_y)) _grasp_search_size_y)
  (:serialization-length
   ()
   (+
    ;; int32 _grasp_search_size_x
    4
    ;; int32 _grasp_search_size_y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _grasp_search_size_x
       (write-long _grasp_search_size_x s)
     ;; int32 _grasp_search_size_y
       (write-long _grasp_search_size_y s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _grasp_search_size_x
     (setq _grasp_search_size_x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _grasp_search_size_y
     (setq _grasp_search_size_y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass haf_grasping::GraspSearchRectangleSizeResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::GraspSearchRectangleSizeResponse
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

(defclass haf_grasping::GraspSearchRectangleSize
  :super ros::object
  :slots ())

(setf (get haf_grasping::GraspSearchRectangleSize :md5sum-) "10248c1006719d0893af769fe3ad61ba")
(setf (get haf_grasping::GraspSearchRectangleSize :datatype-) "haf_grasping/GraspSearchRectangleSize")
(setf (get haf_grasping::GraspSearchRectangleSize :request) haf_grasping::GraspSearchRectangleSizeRequest)
(setf (get haf_grasping::GraspSearchRectangleSize :response) haf_grasping::GraspSearchRectangleSizeResponse)

(defmethod haf_grasping::GraspSearchRectangleSizeRequest
  (:response () (instance haf_grasping::GraspSearchRectangleSizeResponse :init)))

(setf (get haf_grasping::GraspSearchRectangleSizeRequest :md5sum-) "10248c1006719d0893af769fe3ad61ba")
(setf (get haf_grasping::GraspSearchRectangleSizeRequest :datatype-) "haf_grasping/GraspSearchRectangleSizeRequest")
(setf (get haf_grasping::GraspSearchRectangleSizeRequest :definition-)
      "int32 grasp_search_size_x
int32 grasp_search_size_y
---
bool result

")

(setf (get haf_grasping::GraspSearchRectangleSizeResponse :md5sum-) "10248c1006719d0893af769fe3ad61ba")
(setf (get haf_grasping::GraspSearchRectangleSizeResponse :datatype-) "haf_grasping/GraspSearchRectangleSizeResponse")
(setf (get haf_grasping::GraspSearchRectangleSizeResponse :definition-)
      "int32 grasp_search_size_x
int32 grasp_search_size_y
---
bool result

")



(provide :haf_grasping/GraspSearchRectangleSize "10248c1006719d0893af769fe3ad61ba")


