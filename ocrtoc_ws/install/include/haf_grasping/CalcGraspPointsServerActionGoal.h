// Generated by gencpp from file haf_grasping/CalcGraspPointsServerActionGoal.msg
// DO NOT EDIT!


#ifndef HAF_GRASPING_MESSAGE_CALCGRASPPOINTSSERVERACTIONGOAL_H
#define HAF_GRASPING_MESSAGE_CALCGRASPPOINTSSERVERACTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <haf_grasping/CalcGraspPointsServerGoal.h>

namespace haf_grasping
{
template <class ContainerAllocator>
struct CalcGraspPointsServerActionGoal_
{
  typedef CalcGraspPointsServerActionGoal_<ContainerAllocator> Type;

  CalcGraspPointsServerActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  CalcGraspPointsServerActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::haf_grasping::CalcGraspPointsServerGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct CalcGraspPointsServerActionGoal_

typedef ::haf_grasping::CalcGraspPointsServerActionGoal_<std::allocator<void> > CalcGraspPointsServerActionGoal;

typedef boost::shared_ptr< ::haf_grasping::CalcGraspPointsServerActionGoal > CalcGraspPointsServerActionGoalPtr;
typedef boost::shared_ptr< ::haf_grasping::CalcGraspPointsServerActionGoal const> CalcGraspPointsServerActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator1> & lhs, const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator1> & lhs, const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace haf_grasping

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "38bb5a53c06a9410f41de298e209e6e5";
  }

  static const char* value(const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x38bb5a53c06a9410ULL;
  static const uint64_t static_value2 = 0xf41de298e209e6e5ULL;
};

template<class ContainerAllocator>
struct DataType< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "haf_grasping/CalcGraspPointsServerActionGoal";
  }

  static const char* value(const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"CalcGraspPointsServerGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: haf_grasping/CalcGraspPointsServerGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Define the input for grasp calculation: a point cloud\n"
"haf_grasping/GraspInput graspinput\n"
"\n"
"================================================================================\n"
"MSG: haf_grasping/GraspInput\n"
"\n"
"#Header header                        	# header for time/frame information\n"
"sensor_msgs/PointCloud2 input_pc     	# defines the point cloud on which grasps should be calculated (objects)\n"
"string goal_frame_id				 	# the frame_id to which the point cloud should be transformed before grasps are calculated\n"
"geometry_msgs/Point grasp_area_center 	# center of the region where grasps are searched\n"
"float32 grasp_area_length_x				# defines the length of the rectangle (in x direction (in m)) where grasps are searched (with center grasp_area_center)\n"
"float32 grasp_area_length_y				# defines the length of the rectangle (in y direction (in m)) where grasps are searched (with center grasp_area_center)\n"
"\n"
"\n"
"duration max_calculation_time			# maximal calculation time before grasp result is returned\n"
"bool show_only_best_grasp				# If true, only the best grasp is shown in visualization\n"
"int32 threshold_grasp_evaluation		# defines the threshold for return_first_grasp_over_th if it is set to true (otherwise it is ignored)\n"
"\n"
"geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed \n"
"int32 gripper_opening_width				# defines the factor (actually 1/factor) that is used for pre-grasp opening gripper width \n"
"\n"
"#geometry_msgs/Vector3 scale_gripper	# Scale of the gripper in x and y direction if it deviates from a gripper of the size of a huMAN hand\n"
"\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointCloud2\n"
"# This message holds a collection of N-dimensional points, which may\n"
"# contain additional information such as normals, intensity, etc. The\n"
"# point data is stored as a binary blob, its layout described by the\n"
"# contents of the \"fields\" array.\n"
"\n"
"# The point cloud data may be organized 2d (image-like) or 1d\n"
"# (unordered). Point clouds organized as 2d images may be produced by\n"
"# camera depth sensors such as stereo or time-of-flight.\n"
"\n"
"# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n"
"# points).\n"
"Header header\n"
"\n"
"# 2D structure of the point cloud. If the cloud is unordered, height is\n"
"# 1 and width is the length of the point cloud.\n"
"uint32 height\n"
"uint32 width\n"
"\n"
"# Describes the channels and their layout in the binary data blob.\n"
"PointField[] fields\n"
"\n"
"bool    is_bigendian # Is this data bigendian?\n"
"uint32  point_step   # Length of a point in bytes\n"
"uint32  row_step     # Length of a row in bytes\n"
"uint8[] data         # Actual point data, size is (row_step*height)\n"
"\n"
"bool is_dense        # True if there are no invalid points\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointField\n"
"# This message holds the description of one point entry in the\n"
"# PointCloud2 message format.\n"
"uint8 INT8    = 1\n"
"uint8 UINT8   = 2\n"
"uint8 INT16   = 3\n"
"uint8 UINT16  = 4\n"
"uint8 INT32   = 5\n"
"uint8 UINT32  = 6\n"
"uint8 FLOAT32 = 7\n"
"uint8 FLOAT64 = 8\n"
"\n"
"string name      # Name of field\n"
"uint32 offset    # Offset from start of point struct\n"
"uint8  datatype  # Datatype enumeration, see above\n"
"uint32 count     # How many elements in the field\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CalcGraspPointsServerActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::haf_grasping::CalcGraspPointsServerActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::haf_grasping::CalcGraspPointsServerGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HAF_GRASPING_MESSAGE_CALCGRASPPOINTSSERVERACTIONGOAL_H