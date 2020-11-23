
(cl:in-package :asdf)

(defsystem "haf_grasping-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CalcGraspPointsServerAction" :depends-on ("_package_CalcGraspPointsServerAction"))
    (:file "_package_CalcGraspPointsServerAction" :depends-on ("_package"))
    (:file "CalcGraspPointsServerActionFeedback" :depends-on ("_package_CalcGraspPointsServerActionFeedback"))
    (:file "_package_CalcGraspPointsServerActionFeedback" :depends-on ("_package"))
    (:file "CalcGraspPointsServerActionGoal" :depends-on ("_package_CalcGraspPointsServerActionGoal"))
    (:file "_package_CalcGraspPointsServerActionGoal" :depends-on ("_package"))
    (:file "CalcGraspPointsServerActionResult" :depends-on ("_package_CalcGraspPointsServerActionResult"))
    (:file "_package_CalcGraspPointsServerActionResult" :depends-on ("_package"))
    (:file "CalcGraspPointsServerFeedback" :depends-on ("_package_CalcGraspPointsServerFeedback"))
    (:file "_package_CalcGraspPointsServerFeedback" :depends-on ("_package"))
    (:file "CalcGraspPointsServerGoal" :depends-on ("_package_CalcGraspPointsServerGoal"))
    (:file "_package_CalcGraspPointsServerGoal" :depends-on ("_package"))
    (:file "CalcGraspPointsServerResult" :depends-on ("_package_CalcGraspPointsServerResult"))
    (:file "_package_CalcGraspPointsServerResult" :depends-on ("_package"))
    (:file "GraspInput" :depends-on ("_package_GraspInput"))
    (:file "_package_GraspInput" :depends-on ("_package"))
    (:file "GraspOutput" :depends-on ("_package_GraspOutput"))
    (:file "_package_GraspOutput" :depends-on ("_package"))
  ))