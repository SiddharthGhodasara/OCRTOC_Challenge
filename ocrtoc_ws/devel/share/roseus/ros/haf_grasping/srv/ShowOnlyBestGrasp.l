;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::ShowOnlyBestGrasp)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'ShowOnlyBestGrasp (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::SHOWONLYBESTGRASP")
  (make-package "HAF_GRASPING::SHOWONLYBESTGRASP"))
(unless (find-package "HAF_GRASPING::SHOWONLYBESTGRASPREQUEST")
  (make-package "HAF_GRASPING::SHOWONLYBESTGRASPREQUEST"))
(unless (find-package "HAF_GRASPING::SHOWONLYBESTGRASPRESPONSE")
  (make-package "HAF_GRASPING::SHOWONLYBESTGRASPRESPONSE"))

(in-package "ROS")





(defclass haf_grasping::ShowOnlyBestGraspRequest
  :super ros::object
  :slots (_show_only_best_grasp ))

(defmethod haf_grasping::ShowOnlyBestGraspRequest
  (:init
   (&key
    ((:show_only_best_grasp __show_only_best_grasp) nil)
    )
   (send-super :init)
   (setq _show_only_best_grasp __show_only_best_grasp)
   self)
  (:show_only_best_grasp
   (&optional __show_only_best_grasp)
   (if __show_only_best_grasp (setq _show_only_best_grasp __show_only_best_grasp)) _show_only_best_grasp)
  (:serialization-length
   ()
   (+
    ;; bool _show_only_best_grasp
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _show_only_best_grasp
       (if _show_only_best_grasp (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _show_only_best_grasp
     (setq _show_only_best_grasp (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass haf_grasping::ShowOnlyBestGraspResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::ShowOnlyBestGraspResponse
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

(defclass haf_grasping::ShowOnlyBestGrasp
  :super ros::object
  :slots ())

(setf (get haf_grasping::ShowOnlyBestGrasp :md5sum-) "c13d71448b4276a64c7f5417c0cd390a")
(setf (get haf_grasping::ShowOnlyBestGrasp :datatype-) "haf_grasping/ShowOnlyBestGrasp")
(setf (get haf_grasping::ShowOnlyBestGrasp :request) haf_grasping::ShowOnlyBestGraspRequest)
(setf (get haf_grasping::ShowOnlyBestGrasp :response) haf_grasping::ShowOnlyBestGraspResponse)

(defmethod haf_grasping::ShowOnlyBestGraspRequest
  (:response () (instance haf_grasping::ShowOnlyBestGraspResponse :init)))

(setf (get haf_grasping::ShowOnlyBestGraspRequest :md5sum-) "c13d71448b4276a64c7f5417c0cd390a")
(setf (get haf_grasping::ShowOnlyBestGraspRequest :datatype-) "haf_grasping/ShowOnlyBestGraspRequest")
(setf (get haf_grasping::ShowOnlyBestGraspRequest :definition-)
      "bool show_only_best_grasp			# ShowOnlyBestGrasp: defines if only the best grasp should be visualized
---
bool result

")

(setf (get haf_grasping::ShowOnlyBestGraspResponse :md5sum-) "c13d71448b4276a64c7f5417c0cd390a")
(setf (get haf_grasping::ShowOnlyBestGraspResponse :datatype-) "haf_grasping/ShowOnlyBestGraspResponse")
(setf (get haf_grasping::ShowOnlyBestGraspResponse :definition-)
      "bool show_only_best_grasp			# ShowOnlyBestGrasp: defines if only the best grasp should be visualized
---
bool result

")



(provide :haf_grasping/ShowOnlyBestGrasp "c13d71448b4276a64c7f5417c0cd390a")


