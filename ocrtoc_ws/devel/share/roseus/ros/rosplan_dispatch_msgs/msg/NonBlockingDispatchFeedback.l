;; Auto-generated. Do not edit!


(when (boundp 'rosplan_dispatch_msgs::NonBlockingDispatchFeedback)
  (if (not (find-package "ROSPLAN_DISPATCH_MSGS"))
    (make-package "ROSPLAN_DISPATCH_MSGS"))
  (shadow 'NonBlockingDispatchFeedback (find-package "ROSPLAN_DISPATCH_MSGS")))
(unless (find-package "ROSPLAN_DISPATCH_MSGS::NONBLOCKINGDISPATCHFEEDBACK")
  (make-package "ROSPLAN_DISPATCH_MSGS::NONBLOCKINGDISPATCHFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude NonBlockingDispatchFeedback.msg.html


(defclass rosplan_dispatch_msgs::NonBlockingDispatchFeedback
  :super ros::object
  :slots (_feedback ))

(defmethod rosplan_dispatch_msgs::NonBlockingDispatchFeedback
  (:init
   (&key
    ((:feedback __feedback) (instance rosplan_dispatch_msgs::ActionFeedback :init))
    )
   (send-super :init)
   (setq _feedback __feedback)
   self)
  (:feedback
   (&rest __feedback)
   (if (keywordp (car __feedback))
       (send* _feedback __feedback)
     (progn
       (if __feedback (setq _feedback (car __feedback)))
       _feedback)))
  (:serialization-length
   ()
   (+
    ;; rosplan_dispatch_msgs/ActionFeedback _feedback
    (send _feedback :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; rosplan_dispatch_msgs/ActionFeedback _feedback
       (send _feedback :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; rosplan_dispatch_msgs/ActionFeedback _feedback
     (send _feedback :deserialize buf ptr-) (incf ptr- (send _feedback :serialization-length))
   ;;
   self)
  )

(setf (get rosplan_dispatch_msgs::NonBlockingDispatchFeedback :md5sum-) "c100388b79a4f0ef9c6019135b83a757")
(setf (get rosplan_dispatch_msgs::NonBlockingDispatchFeedback :datatype-) "rosplan_dispatch_msgs/NonBlockingDispatchFeedback")
(setf (get rosplan_dispatch_msgs::NonBlockingDispatchFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
rosplan_dispatch_msgs/ActionFeedback feedback


================================================================================
MSG: rosplan_dispatch_msgs/ActionFeedback
#actionFeedback message
int32 action_id
string status
diagnostic_msgs/KeyValue[] information

================================================================================
MSG: diagnostic_msgs/KeyValue
string key # what to label this value when viewing
string value # a value to track over time

")



(provide :rosplan_dispatch_msgs/NonBlockingDispatchFeedback "c100388b79a4f0ef9c6019135b83a757")

