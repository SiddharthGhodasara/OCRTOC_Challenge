
(cl:in-package :asdf)

(defsystem "haf_grasping-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "GraspApproachVector" :depends-on ("_package_GraspApproachVector"))
    (:file "_package_GraspApproachVector" :depends-on ("_package"))
    (:file "GraspCalculationTimeMax" :depends-on ("_package_GraspCalculationTimeMax"))
    (:file "_package_GraspCalculationTimeMax" :depends-on ("_package"))
    (:file "GraspPreGripperOpeningWidth" :depends-on ("_package_GraspPreGripperOpeningWidth"))
    (:file "_package_GraspPreGripperOpeningWidth" :depends-on ("_package"))
    (:file "GraspSearchCenter" :depends-on ("_package_GraspSearchCenter"))
    (:file "_package_GraspSearchCenter" :depends-on ("_package"))
    (:file "GraspSearchRectangleSize" :depends-on ("_package_GraspSearchRectangleSize"))
    (:file "_package_GraspSearchRectangleSize" :depends-on ("_package"))
    (:file "ShowOnlyBestGrasp" :depends-on ("_package_ShowOnlyBestGrasp"))
    (:file "_package_ShowOnlyBestGrasp" :depends-on ("_package"))
  ))