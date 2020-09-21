;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspCalculationTimeMax)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspCalculationTimeMax (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAX")
  (make-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAX"))
(unless (find-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAXREQUEST")
  (make-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAXREQUEST"))
(unless (find-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAXRESPONSE")
  (make-package "HAF_GRASPING::GRASPCALCULATIONTIMEMAXRESPONSE"))

(in-package "ROS")





(defclass haf_grasping::GraspCalculationTimeMaxRequest
  :super ros::object
  :slots (_max_calculation_time ))

(defmethod haf_grasping::GraspCalculationTimeMaxRequest
  (:init
   (&key
    ((:max_calculation_time __max_calculation_time) (instance ros::time :init))
    )
   (send-super :init)
   (setq _max_calculation_time __max_calculation_time)
   self)
  (:max_calculation_time
   (&optional __max_calculation_time)
   (if __max_calculation_time (setq _max_calculation_time __max_calculation_time)) _max_calculation_time)
  (:serialization-length
   ()
   (+
    ;; duration _max_calculation_time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; duration _max_calculation_time
       (write-long (send _max_calculation_time :sec) s) (write-long (send _max_calculation_time :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; duration _max_calculation_time
     (send _max_calculation_time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _max_calculation_time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass haf_grasping::GraspCalculationTimeMaxResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::GraspCalculationTimeMaxResponse
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

(defclass haf_grasping::GraspCalculationTimeMax
  :super ros::object
  :slots ())

(setf (get haf_grasping::GraspCalculationTimeMax :md5sum-) "fe39c4e255168ec5afaa585fcfbd448f")
(setf (get haf_grasping::GraspCalculationTimeMax :datatype-) "haf_grasping/GraspCalculationTimeMax")
(setf (get haf_grasping::GraspCalculationTimeMax :request) haf_grasping::GraspCalculationTimeMaxRequest)
(setf (get haf_grasping::GraspCalculationTimeMax :response) haf_grasping::GraspCalculationTimeMaxResponse)

(defmethod haf_grasping::GraspCalculationTimeMaxRequest
  (:response () (instance haf_grasping::GraspCalculationTimeMaxResponse :init)))

(setf (get haf_grasping::GraspCalculationTimeMaxRequest :md5sum-) "fe39c4e255168ec5afaa585fcfbd448f")
(setf (get haf_grasping::GraspCalculationTimeMaxRequest :datatype-) "haf_grasping/GraspCalculationTimeMaxRequest")
(setf (get haf_grasping::GraspCalculationTimeMaxRequest :definition-)
      "duration max_calculation_time			# maximal calculation time before grasp result is returned
---
bool result

")

(setf (get haf_grasping::GraspCalculationTimeMaxResponse :md5sum-) "fe39c4e255168ec5afaa585fcfbd448f")
(setf (get haf_grasping::GraspCalculationTimeMaxResponse :datatype-) "haf_grasping/GraspCalculationTimeMaxResponse")
(setf (get haf_grasping::GraspCalculationTimeMaxResponse :definition-)
      "duration max_calculation_time			# maximal calculation time before grasp result is returned
---
bool result

")



(provide :haf_grasping/GraspCalculationTimeMax "fe39c4e255168ec5afaa585fcfbd448f")


