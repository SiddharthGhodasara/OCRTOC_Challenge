/*
 * David Fischinger - Vienna University of Technology
 * March 2015
 *
 * ** Grasp Action Client - for Testing **
 *
 * This node is serving as a client for the calculation of grasp points
 * based on the action server for grasp calculation.
 * This nodes subscribes to the topic /haf_grasping/depth_registered/single_cloud/points_in_lcs (lcs: local coordinate system)
 * and receives (single) point clouds (in a local coordinate system where z is perpendicular to the floor).
 * The node sends the point cloud as an action server goal and receives the grasp result.
 *
 */


//ROS includes
#include <ros/ros.h>
#include <ros/package.h>
#include "std_msgs/String.h"
#include "sensor_msgs/PointCloud2.h"
#include <geometry_msgs/Point.h>
#include <geometry_msgs/Vector3.h>
//actionlib
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
//grasp action message
#include <haf_grasping/CalcGraspPointsServerAction.h>
// service messages
#include <haf_grasping/GraspSearchCenter.h>
#include <haf_grasping/GraspSearchRectangleSize.h>
#include <haf_grasping/GraspCalculationTimeMax.h>
#include <haf_grasping/GraspApproachVector.h>
#include <haf_grasping/ShowOnlyBestGrasp.h>
#include <haf_grasping/GraspPreGripperOpeningWidth.h>
// for reading pcd file
#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include "pcl_ros/transforms.h"
#include <pcl_ros/point_cloud.h>
//#include "pcl/io/io.h"
//#include <boost/thread/thread.hpp>
#include <boost/bind.hpp>
#include <boost/date_time.hpp>
#include <boost/algorithm/string.hpp>
#include <bits/stdc++.h>

class CCalcGrasppointsClient
{
public:
	ros::Subscriber pc_sub;								//subscriber for pointcloud
	ros::Subscriber pcd_sub;
	ros::Subscriber coord_sub;							//subscriber for path for pcd-file (to read)
	ros::ServiceServer srv_set_grasp_center;			// service to set new grasp center (center of rectangles where grasps are searched for)
	ros::ServiceServer srv_set_grasp_search_area_size;	// service to set size of rectangle where grasps are searched
	ros::ServiceServer srv_set_grasp_calculation_time_max;	// service to set maximal grasp calculation time (sec) before result is returned
	ros::ServiceServer srv_set_approach_vector;			// service to set approach vector for grasping (only direction hand is approaching, not roll angle)
	ros::ServiceServer srv_set_show_only_best_grasp;	// service to set show_only_best_grasp bool variable
	ros::ServiceServer srv_set_gripper_width;			// service to set factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f
	geometry_msgs::Point graspsearchcenter;				// center for searching for grasps
	geometry_msgs::Vector3 approach_vector;				// defines the direction from where a grasp should be executed
	int grasp_search_size_x;			// the size (x direction) where grasps are really calculated (in each direction 7cm more are needed for feature calculation!
	int grasp_search_size_y;			// the size (y direction) where grasps are really calculated (in each direction 7cm more are needed for feature calculation!
	int max_grasp_search_size_x;	// x-limit for grasp search area size
	int max_grasp_search_size_y;	// y-limit for grasp search area size
	ros::Duration grasp_calculation_time_max;	//max time used for grasp calculation (sec) before result is returned
	bool show_only_best_grasp;
	std::string base_frame_default;
	int gripper_opening_width; 			//defines pre-grasp gripper opening width

	void get_coord_cb(const geometry_msgs::PointStamped::ConstPtr& msg);
	void get_grasp_cb(const sensor_msgs::PointCloud2ConstPtr& pc_in);
	void open_pcd_and_trig_get_grasp_cb(std_msgs::String pcd_path);
	bool set_grasp_center(haf_grasping::GraspSearchCenter::Request &req, haf_grasping::GraspSearchCenter::Response &res);
	bool set_grasp_search_area_size(haf_grasping::GraspSearchRectangleSize::Request &req, haf_grasping::GraspSearchRectangleSize::Response &res);
	bool set_grasp_calculation_time_max(haf_grasping::GraspCalculationTimeMax::Request &req, haf_grasping::GraspCalculationTimeMax::Response &res);
	bool set_approach_vector(haf_grasping::GraspApproachVector::Request &req, haf_grasping::GraspApproachVector::Response &res);
	bool set_show_only_best_grasp(haf_grasping::ShowOnlyBestGrasp::Request &req, haf_grasping::ShowOnlyBestGrasp::Response &res);
	bool set_gripper_width(haf_grasping::GraspPreGripperOpeningWidth::Request &req,	haf_grasping::GraspPreGripperOpeningWidth::Response &res);

	CCalcGrasppointsClient(ros::NodeHandle nh_)
	{
		//ROS_INFO("NOOOOO!!!!!!");
		this->graspsearchcenter.x = -1;
		nh_.param("grasp_search_size_x", this->grasp_search_size_x, 18);	//default value = max. limit 32
		nh_.param("grasp_search_size_y", this->grasp_search_size_y, 30);	//default value = max. limit 44
		this->coord_sub = nh_.subscribe("/pose", 1, &CCalcGrasppointsClient::get_coord_cb, this);
		//define center of grasp search rectangle (respectively take from launch file)
		//define grasp approach direction (respectively take from launch file)
		this->approach_vector.x = this->approach_vector.y = 0.0;
		this->approach_vector.z = 1.0;
		std::vector<float> gripper_approach_vector_tmp;
		if ( nh_.getParam("gripper_approach_vector", gripper_approach_vector_tmp) ) {
			this->approach_vector.x = gripper_approach_vector_tmp[0];
			this->approach_vector.y = gripper_approach_vector_tmp[1];
			this->approach_vector.z = gripper_approach_vector_tmp[2];
		}

		//define size of grasp search rectangle (respectively take from launch file)

		//ROS_INFO_STREAM("Search size" <<grasp_search_size_y << grasp_search_size_x);
		// define maximal time before grasp result is returned
		int max_calculation_time;
		nh_.param("max_calculation_time", max_calculation_time, 50);	// in sec, with default value 50
		this->grasp_calculation_time_max = ros::Duration(max_calculation_time);

		// define if only the best grasp should be visualized (respectively take bool value from launch file)
		nh_.param("show_only_best_grasp", this->show_only_best_grasp, true);

		// set default cloud frame (if cloud is generated from pcd)
		nh_.param("base_frame", this->base_frame_default, std::string("world"));
		// set gripper opening with factor => 1/gripper opening width is tested
		nh_.param("gripper_width", this->gripper_opening_width, 1);


		//subscriber for the point cloud
		std::string input_pc_topic = "/haf_grasping/depth_registered/single_cloud/points_in_lcs";
		nh_.param("input_pc_topic", input_pc_topic, input_pc_topic);
		this->pc_sub = nh_.subscribe(input_pc_topic,1, &CCalcGrasppointsClient::get_grasp_cb, this);
		this->pcd_sub = nh_.subscribe("/haf_grasping/input_pcd_rcs_path",1, &CCalcGrasppointsClient::open_pcd_and_trig_get_grasp_cb, this);
		//services for setting parameters
		this->srv_set_grasp_center = nh_.advertiseService("/haf_grasping/set_grasp_center", &CCalcGrasppointsClient::set_grasp_center,this);
		this->srv_set_grasp_search_area_size = nh_.advertiseService("/haf_grasping/set_grasp_search_area_size", &CCalcGrasppointsClient::set_grasp_search_area_size,this);
		this->srv_set_grasp_calculation_time_max = nh_.advertiseService("/haf_grasping/set_grasp_calculation_time_max", &CCalcGrasppointsClient::set_grasp_calculation_time_max,this);
		this->srv_set_approach_vector = nh_.advertiseService("/haf_grasping/set_approach_vector", &CCalcGrasppointsClient::set_approach_vector, this);
		this->srv_set_show_only_best_grasp = nh_.advertiseService("/haf_grasping/set_show_only_best_grasp", &CCalcGrasppointsClient::set_show_only_best_grasp, this);
		this->srv_set_gripper_width = nh_.advertiseService("/haf_grasping/set_gripper_opening_width", &CCalcGrasppointsClient::set_gripper_width, this);
	}
};

// define goal (input) for grasp calculation, send it to grasp action server and receive result
void CCalcGrasppointsClient::get_coord_cb(const geometry_msgs::PointStamped::ConstPtr& msg)
{
	//ROS_INFO("Coord Callback");
	//Extracting the header
	std::string str;
	std::vector<std::string> result;
	//Storing the frame id  in another variables
	str = msg->header.frame_id;
	//Spliting the string with , as delimiter
	boost::split(result, str, boost::is_any_of(","));
	//Converting theextracted coordinates to float
	float xx = std::stof(result[1]);
	float yy = std::stof(result[2]);
	//Changing the units from m to cm
	xx *= 100;
	yy *= 100;
	//Assigning the value to class variables
	this->grasp_search_size_x = 18;
	this->grasp_search_size_y = 30;
	this->max_grasp_search_size_x = 18;				//max. limit 32-14=18
	this->max_grasp_search_size_y = 30;				//max. limit 44-14=30
	if (this->grasp_search_size_x < 1 or this->grasp_search_size_x >= this->max_grasp_search_size_x)
		this->grasp_search_size_x = 7;
	if (this->grasp_search_size_y < 1 or this->grasp_search_size_y >= this->max_grasp_search_size_y)
		this->grasp_search_size_y = 7;
	//ROS_INFO_STREAM("The correct Search size is: " <<this->grasp_search_size_y << this->grasp_search_size_x);
	//Extracting the coordinates
	this->graspsearchcenter.x = msg->point.x;
	this->graspsearchcenter.y = msg->point.y;
	this->graspsearchcenter.z = 0; //msg->point.z;

	//ROS_INFO_STREAM("coordinates of yolo x"<<this->graspsearchcenter.x);
	//ROS_INFO_STREAM("coordinates of yolo y"<<this->graspsearchcenter.y);
}

// open pcd file for given path and start get_grasp_cb (that triggers grasp calculation)
void CCalcGrasppointsClient::open_pcd_and_trig_get_grasp_cb(std_msgs::String pcd_path)
{
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);


  if (pcl::io::loadPCDFile<pcl::PointXYZ> (pcd_path.data.c_str(), *cloud) == -1) //* load the file
  {
    PCL_ERROR ("Couldn't read input file (pcd) \n");
    return;
  }
  // std::cout << "Loaded "
  //          << cloud->width * cloud->height
  //          << " data points from " << pcd_path.data.c_str();

  //transform pcl to ros-msg
  sensor_msgs::PointCloud2 pcd_as_ros_msg;// = new sensor_msgs::PointCloud2ConstPtr();
  pcl::toROSMsg(*cloud, pcd_as_ros_msg);
  pcd_as_ros_msg.header.frame_id = this->base_frame_default /*"base_link"*/;
  pcd_as_ros_msg.header.stamp = ros::Time(0);
  const sensor_msgs::PointCloud2ConstPtr pcd_as_ros_msg_const_ptr = boost::make_shared<sensor_msgs::PointCloud2>(pcd_as_ros_msg);
  CCalcGrasppointsClient::get_grasp_cb(pcd_as_ros_msg_const_ptr);
}

// define goal (input) for grasp calculation, send it to grasp action server and receive result
void CCalcGrasppointsClient::get_grasp_cb(const sensor_msgs::PointCloud2ConstPtr& pc_in)
{
		//ROS_INFO("\nFrom calc_grasppoints_action_client: point cloud received");

		// create the action client
		// true causes the client to spin its own thread
		actionlib::SimpleActionClient<haf_grasping::CalcGraspPointsServerAction> ac("calc_grasppoints_svm_action_server", true);

		//ROS_INFO("Waiting for action server to start.");
		// wait for the action server to start
		ac.waitForServer(); //will wait for infinite time

		//ROS_INFO("Action server started, sending goal.");
		// send a goal to the action
		haf_grasping::CalcGraspPointsServerGoal goal;
		goal.graspinput.input_pc = *pc_in;

		goal.graspinput.grasp_area_center = this->graspsearchcenter;

		//set grasp approach vector
		goal.graspinput.approach_vector = this->approach_vector;

		// set size of grasp search area
		goal.graspinput.grasp_area_length_x = this->grasp_search_size_x+14;
		goal.graspinput.grasp_area_length_y = this->grasp_search_size_y+14;

		// set max grasp calculation time
		goal.graspinput.max_calculation_time = this->grasp_calculation_time_max;

		// set if only best grasp should be visualized
		goal.graspinput.show_only_best_grasp = this->show_only_best_grasp;

		// set pre-grasp gripper opening width (factor for scaling pc)
		goal.graspinput.gripper_opening_width = this->gripper_opening_width;

		//send goal
		ac.sendGoal(goal);

		//wait for the action to return
		bool finished_before_timeout = ac.waitForResult(ros::Duration(50.0));

		if (finished_before_timeout)
		{
			actionlib::SimpleClientGoalState state = ac.getState();
			boost::shared_ptr<const haf_grasping::CalcGraspPointsServerResult_<std::allocator<void> > > result = ac.getResult();
			//ROS_INFO_STREAM("Result: %s" << (*(result)).graspOutput);
			//ROS_INFO("Action finished: %s",state.toString().c_str());
		}
		//else
			//ROS_INFO("Action did not finish before the time out.");
}


//set grasp search center
bool CCalcGrasppointsClient::set_grasp_center(haf_grasping::GraspSearchCenter::Request &req,
		haf_grasping::GraspSearchCenter::Response &res)
{
	//set grasp search center
	this->graspsearchcenter.x = req.graspsearchcenter.x;
	this->graspsearchcenter.y = req.graspsearchcenter.y;
	this->graspsearchcenter.z = req.graspsearchcenter.z;
	//ROS_INFO("Set grasp search center to: x=%f, y=%f, z=%f", req.graspsearchcenter.x, req.graspsearchcenter.y, req.graspsearchcenter.z);
	res.result = true;
	//ROS_INFO("sending back response: [%ld]", (long int)res.result);
	return res.result;
}

//set size of rectangle where grasps are searched
bool CCalcGrasppointsClient::set_grasp_search_area_size(haf_grasping::GraspSearchRectangleSize::Request &req,
		haf_grasping::GraspSearchRectangleSize::Response &res)
{
	//set grasp search rectangle size
	if (req.grasp_search_size_x >= 0 and req.grasp_search_size_x <= this->max_grasp_search_size_x){
		this->grasp_search_size_x = req.grasp_search_size_x;
		//ROS_INFO("Set grasp rectangle size to: x=%ld", (long int)req.grasp_search_size_x);
	} else {
		//ROS_INFO("Could not set grasp rectangle size for x. Allowed values: [0, %ld ]. Received value was: x=%ld", (long int)this->max_grasp_search_size_x,(long int)req.grasp_search_size_x);
		res.result = false;
		return res.result;
	}
	if (req.grasp_search_size_y >= 0 and req.grasp_search_size_y <= this->max_grasp_search_size_y){
		this->grasp_search_size_y = req.grasp_search_size_y;
		//ROS_INFO("Set grasp rectangle size to: y=%ld", (long int)req.grasp_search_size_y);
	} else {
		//ROS_INFO("Could not set grasp rectangle size for y. Allowed values: [0, %ld ]. Received value was: y=%ld", (long int)this->max_grasp_search_size_y,(long int)req.grasp_search_size_y);
		res.result = false;
		return res.result;
	}

	res.result = true;
	//ROS_INFO("sending back response: [%ld]", (long int)res.result);
	return res.result;
}


//set maximal grasp calculation time before result has to be returned
bool CCalcGrasppointsClient::set_grasp_calculation_time_max(haf_grasping::GraspCalculationTimeMax::Request &req,
		haf_grasping::GraspCalculationTimeMax::Response &res)
{
	//set max grasp calculation time
	this->grasp_calculation_time_max = req.max_calculation_time;
	//ROS_INFO("Set max calculation time (sec) to: x=%d", (int)req.max_calculation_time.toSec());
	res.result = true;
	//ROS_INFO("sending back response: [%d]", (int)res.result);
	return res.result;
}

//set approach vector for approaching the object with gripper
bool CCalcGrasppointsClient::set_approach_vector(haf_grasping::GraspApproachVector::Request &req, haf_grasping::GraspApproachVector::Response &res)
{
	//set grasp approach vector
	this->approach_vector = req.approach_vector;
	//ROS_INFO("Set approach vector to: [%f,%f,%f]", this->approach_vector.x,this->approach_vector.y,this->approach_vector.z);
	res.result = true;
	//ROS_INFO("sending back response: [%d]", (int)res.result);
	return res.result;
}

//set show_only_best_grasp (for visualization)
bool CCalcGrasppointsClient::set_show_only_best_grasp(haf_grasping::ShowOnlyBestGrasp::Request &req,
		haf_grasping::ShowOnlyBestGrasp::Response &res)
{
	//set show_only_best_grasp
	this->show_only_best_grasp = req.show_only_best_grasp;
	//ROS_INFO("Set show_only_best_grasp to: [%d] ", (int)this->show_only_best_grasp);
	res.result = true;
	//ROS_INFO("sending back response: [%d]", (int)res.result);
	return res.result;
}

//set maximal grasp calculation time before result has to be returned
bool CCalcGrasppointsClient::set_gripper_width(haf_grasping::GraspPreGripperOpeningWidth::Request &req,
		haf_grasping::GraspPreGripperOpeningWidth::Response &res)
{
	//set pre-grasp gripper opening width
	this->gripper_opening_width = req.gripper_opening_width;
	//ROS_INFO("Set gripper_opening_width (factor for scaling pc) to: x=%d", (int)req.gripper_opening_width);
	res.result = true;
	//ROS_INFO("sending back response: [%d]", (int)res.result);
	return res.result;
}

/*
//Global Variable
double x = 0.5, y = 0.5, z = 0.5;

//Callback function for
void callback(const geometry_msgs::PointStamped::ConstPtr& msg, ros::NodeHandle nh)
{
	ROS_INFO("Here");
	//Extracting the header
	std_msgs::String a;
	a.data = msg->header.frame_id;
	//Extracting the coordinates
	x = msg->point.x;
	y = msg->point.y;
	z = msg->point.z;
	ROS_INFO_STREAM(msg->header.frame_id);
	ROS_INFO_STREAM("X" << x);
	ROS_INFO_STREAM("Y" << y);
	ros::Duration(2.0).sleep();
	ROS_INFO("Here");
}
*/
//Main Function
int main (int argc, char **argv)
{
	using boost::bind;
	bool received_js = false;
  //ROS_INFO("ROS NODE calc_grasppoints_client started");
	//Initializing the node
	ros::init(argc, argv, "calc_grasppoint_client");
	//Defining the node handle
	ros::NodeHandle nh_;
	//Subscribing to PointStamped Message
	//ros::Subscriber sub = nh_.subscribe<geometry_msgs::PointStamped>("/pose", 1000, boost::bind(callback, _1, nh_));
	/*while(! received_js)
	{
		received_js = true;
	}
	ROS_INFO_STREAM(x);
	ROS_INFO_STREAM(y);
}*/
	CCalcGrasppointsClient grasp_client(nh_);
	ros::spin();
	return 0;
}
