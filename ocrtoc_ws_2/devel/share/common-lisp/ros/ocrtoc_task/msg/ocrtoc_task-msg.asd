
(cl:in-package :asdf)

(defsystem "ocrtoc_task-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CleanAction" :depends-on ("_package_CleanAction"))
    (:file "_package_CleanAction" :depends-on ("_package"))
    (:file "CleanActionFeedback" :depends-on ("_package_CleanActionFeedback"))
    (:file "_package_CleanActionFeedback" :depends-on ("_package"))
    (:file "CleanActionGoal" :depends-on ("_package_CleanActionGoal"))
    (:file "_package_CleanActionGoal" :depends-on ("_package"))
    (:file "CleanActionResult" :depends-on ("_package_CleanActionResult"))
    (:file "_package_CleanActionResult" :depends-on ("_package"))
    (:file "CleanFeedback" :depends-on ("_package_CleanFeedback"))
    (:file "_package_CleanFeedback" :depends-on ("_package"))
    (:file "CleanGoal" :depends-on ("_package_CleanGoal"))
    (:file "_package_CleanGoal" :depends-on ("_package"))
    (:file "CleanResult" :depends-on ("_package_CleanResult"))
    (:file "_package_CleanResult" :depends-on ("_package"))
  ))