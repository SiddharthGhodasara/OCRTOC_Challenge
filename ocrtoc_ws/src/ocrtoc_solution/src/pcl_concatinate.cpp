//Including Libraries
#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <tf/transform_listener.h>

#include <geometry_msgs/TransformStamped.h>
#include <control_msgs/PointHeadGoal.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/PCLPointCloud2.h>
#include <pcl/PointIndices.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/io/pcd_io.h>
#include <pcl/segmentation/extract_clusters.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <ros/duration.h>
#include <tf/LinearMath/Transform.h>
#include <tf2/exceptions.h>
#include "ros/console.h"
#include <pcl/ModelCoefficients.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/filters/passthrough.h>
#include <pcl/kdtree/kdtree.h>
#include <pcl/point_types_conversion.h>
#include <pcl/segmentation/extract_polygonal_prism_data.h>
#include <pcl/surface/convex_hull.h>
#include <pcl/point_types_conversion.h>
#include <pcl_ros/transforms.h>
#include <pcl/filters/statistical_outlier_removal.h>

//Topics
static const std::string IMAGE_TOPIC = "/realsense/depth/points";
static const std::string PUBLISH_TOPIC = "/pcl/points";

//Publisher
ros::Publisher pub;

//Variable to store concatinated point cloud
pcl::PointCloud<pcl::PointXYZRGB>::Ptr sum_pcPtr(new pcl::PointCloud<pcl::PointXYZRGB>());

//Global Variables for transformations
geometry_msgs::TransformStamped transformStamped;
geometry_msgs::TransformStamped initial_transformStamped;
tf::Transform initial_transform;

//Lookup transform function
geometry_msgs::TransformStamped lookup_transform(std::string target_frame, std::string source_frame)
{
  geometry_msgs::TransformStamped transformStamped;
  try
  {
    transformStamped = tf_buffer_.lookupTransform(target_frame, source_frame, ros::Time::now(), ros::Duration(3.0));
  }
  catch(tf2::TransformException &ex)
  {
    ROS_WARN("%s",ex.what());
    ros::Duration(1.0).sleep();
  }
  //Returning the transformation
  return transformStamped;
}

//Inline funtion to convert Point XYZRGBA to PointXYZRGB
inline void PointCloudXYZRGBAtoXYZRGB(pcl::PointCloud<pcl::PointXYZRGBA>& in, pcl::PointCloud<pcl::PointXYZRGB>& out)
{
  out.width   = in.width;
  out.height  = in.height;
  out.points.resize(in.points.size());
  for (size_t i = 0; i < in.points.size (); i++)
  {
    out.points[i].x = in.points[i].x;
    out.points[i].y = in.points[i].y;
    out.points[i].z = in.points[i].z;
    out.points[i].r = in.points[i].r;
    out.points[i].g = in.points[i].g;
    out.points[i].b = in.points[i].b;
  }
}

//Subscriber Callback function
void callback(const sensor_msgs::PointCloud2ConstPtr& cloud_msg)
{
    //Converting PointCLoud 2 to XYZRGB Point Cloud
    pcl::PCLPointCloud2 pcl_pc2;
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::PointCloud<pcl::PointXYZRGBA> temp_cloud;
    pcl_conversions::toPCL(*cloud_msg, pcl_pc2);
    pcl::fromPCLPointCloud2(pcl_pc2, temp_cloud);
    PointCloudXYZRGBAtoXYZRGB(temp_cloud, *cloud);

    //Applygin transformations
    transformStamped = lookup_transform("base_link", "realSense_link");
    tf::Transform transform;
    tf::transformMsgToTF(transformStamped.transform, transform);
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr transformed_cloud (new pcl::PointCloud<pcl::PointXYZRGB> ());
    pcl_ros::transformPointCloud (*cloud, *transformed_cloud, transform);
    ros::Duration(2.0).sleep();

    //Concatinating the point clouds
    *sum_pcPtr += *transformed_cloud;

    //Converting PCL to PointCloud2D
    sensor_msgs::PointCloud2 output;
    pcl::PCLPointCloud2 outputPCL;
    pcl::toPCLPointCloud2(*transformed_cloud, outputPCL);
    pcl_conversions::fromPCL(outputPCL, output);

    //Publishing the output
    pub.publish (output);
}

//Main Function
int main(int argc, char** argv)
{
  //Initializing the Node
  ros::init(argc, argv, "point_cloud_contact");
  //Defining the node handler object
  ros::NodeHandle node;
  //Subsribing to point cloud topic
  ros::Subscriber sub = node.subscribe(IMAGE_TOPIC, 1, callback);
  // Create a ROS publisher to PUBLISH_TOPIC with a queue_size of 1
  pub = node.advertise<sensor_msgs::PointCloud2>(PUBLISH_TOPIC, 1);
  // Spin
  ros::spin();
  // Success
  return 0;
}
