;; Auto-generated. Do not edit!


(when (boundp 'haf_grasping::GraspPreGripperOpeningWidth)
  (if (not (find-package "HAF_GRASPING"))
    (make-package "HAF_GRASPING"))
  (shadow 'GraspPreGripperOpeningWidth (find-package "HAF_GRASPING")))
(unless (find-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTH")
  (make-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTH"))
(unless (find-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTHREQUEST")
  (make-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTHREQUEST"))
(unless (find-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTHRESPONSE")
  (make-package "HAF_GRASPING::GRASPPREGRIPPEROPENINGWIDTHRESPONSE"))

(in-package "ROS")





(defclass haf_grasping::GraspPreGripperOpeningWidthRequest
  :super ros::object
  :slots (_gripper_opening_width ))

(defmethod haf_grasping::GraspPreGripperOpeningWidthRequest
  (:init
   (&key
    ((:gripper_opening_width __gripper_opening_width) 0)
    )
   (send-super :init)
   (setq _gripper_opening_width (round __gripper_opening_width))
   self)
  (:gripper_opening_width
   (&optional __gripper_opening_width)
   (if __gripper_opening_width (setq _gripper_opening_width __gripper_opening_width)) _gripper_opening_width)
  (:serialization-length
   ()
   (+
    ;; int32 _gripper_opening_width
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _gripper_opening_width
       (write-long _gripper_opening_width s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _gripper_opening_width
     (setq _gripper_opening_width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass haf_grasping::GraspPreGripperOpeningWidthResponse
  :super ros::object
  :slots (_result ))

(defmethod haf_grasping::GraspPreGripperOpeningWidthResponse
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

(defclass haf_grasping::GraspPreGripperOpeningWidth
  :super ros::object
  :slots ())

(setf (get haf_grasping::GraspPreGripperOpeningWidth :md5sum-) "01233f977ab6b3bc3035826d00041c09")
(setf (get haf_grasping::GraspPreGripperOpeningWidth :datatype-) "haf_grasping/GraspPreGripperOpeningWidth")
(setf (get haf_grasping::GraspPreGripperOpeningWidth :request) haf_grasping::GraspPreGripperOpeningWidthRequest)
(setf (get haf_grasping::GraspPreGripperOpeningWidth :response) haf_grasping::GraspPreGripperOpeningWidthResponse)

(defmethod haf_grasping::GraspPreGripperOpeningWidthRequest
  (:response () (instance haf_grasping::GraspPreGripperOpeningWidthResponse :init)))

(setf (get haf_grasping::GraspPreGripperOpeningWidthRequest :md5sum-) "01233f977ab6b3bc3035826d00041c09")
(setf (get haf_grasping::GraspPreGripperOpeningWidthRequest :datatype-) "haf_grasping/GraspPreGripperOpeningWidthRequest")
(setf (get haf_grasping::GraspPreGripperOpeningWidthRequest :definition-)
      "int32 gripper_opening_width			# factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f
---
bool result

")

(setf (get haf_grasping::GraspPreGripperOpeningWidthResponse :md5sum-) "01233f977ab6b3bc3035826d00041c09")
(setf (get haf_grasping::GraspPreGripperOpeningWidthResponse :datatype-) "haf_grasping/GraspPreGripperOpeningWidthResponse")
(setf (get haf_grasping::GraspPreGripperOpeningWidthResponse :definition-)
      "int32 gripper_opening_width			# factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f
---
bool result

")



(provide :haf_grasping/GraspPreGripperOpeningWidth "01233f977ab6b3bc3035826d00041c09")


