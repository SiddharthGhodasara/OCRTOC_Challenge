// Auto-generated. Do not edit!

// (in-package haf_grasping.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class GraspInput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.input_pc = null;
      this.goal_frame_id = null;
      this.grasp_area_center = null;
      this.grasp_area_length_x = null;
      this.grasp_area_length_y = null;
      this.max_calculation_time = null;
      this.show_only_best_grasp = null;
      this.threshold_grasp_evaluation = null;
      this.approach_vector = null;
      this.gripper_opening_width = null;
    }
    else {
      if (initObj.hasOwnProperty('input_pc')) {
        this.input_pc = initObj.input_pc
      }
      else {
        this.input_pc = new sensor_msgs.msg.PointCloud2();
      }
      if (initObj.hasOwnProperty('goal_frame_id')) {
        this.goal_frame_id = initObj.goal_frame_id
      }
      else {
        this.goal_frame_id = '';
      }
      if (initObj.hasOwnProperty('grasp_area_center')) {
        this.grasp_area_center = initObj.grasp_area_center
      }
      else {
        this.grasp_area_center = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('grasp_area_length_x')) {
        this.grasp_area_length_x = initObj.grasp_area_length_x
      }
      else {
        this.grasp_area_length_x = 0.0;
      }
      if (initObj.hasOwnProperty('grasp_area_length_y')) {
        this.grasp_area_length_y = initObj.grasp_area_length_y
      }
      else {
        this.grasp_area_length_y = 0.0;
      }
      if (initObj.hasOwnProperty('max_calculation_time')) {
        this.max_calculation_time = initObj.max_calculation_time
      }
      else {
        this.max_calculation_time = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('show_only_best_grasp')) {
        this.show_only_best_grasp = initObj.show_only_best_grasp
      }
      else {
        this.show_only_best_grasp = false;
      }
      if (initObj.hasOwnProperty('threshold_grasp_evaluation')) {
        this.threshold_grasp_evaluation = initObj.threshold_grasp_evaluation
      }
      else {
        this.threshold_grasp_evaluation = 0;
      }
      if (initObj.hasOwnProperty('approach_vector')) {
        this.approach_vector = initObj.approach_vector
      }
      else {
        this.approach_vector = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('gripper_opening_width')) {
        this.gripper_opening_width = initObj.gripper_opening_width
      }
      else {
        this.gripper_opening_width = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspInput
    // Serialize message field [input_pc]
    bufferOffset = sensor_msgs.msg.PointCloud2.serialize(obj.input_pc, buffer, bufferOffset);
    // Serialize message field [goal_frame_id]
    bufferOffset = _serializer.string(obj.goal_frame_id, buffer, bufferOffset);
    // Serialize message field [grasp_area_center]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.grasp_area_center, buffer, bufferOffset);
    // Serialize message field [grasp_area_length_x]
    bufferOffset = _serializer.float32(obj.grasp_area_length_x, buffer, bufferOffset);
    // Serialize message field [grasp_area_length_y]
    bufferOffset = _serializer.float32(obj.grasp_area_length_y, buffer, bufferOffset);
    // Serialize message field [max_calculation_time]
    bufferOffset = _serializer.duration(obj.max_calculation_time, buffer, bufferOffset);
    // Serialize message field [show_only_best_grasp]
    bufferOffset = _serializer.bool(obj.show_only_best_grasp, buffer, bufferOffset);
    // Serialize message field [threshold_grasp_evaluation]
    bufferOffset = _serializer.int32(obj.threshold_grasp_evaluation, buffer, bufferOffset);
    // Serialize message field [approach_vector]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.approach_vector, buffer, bufferOffset);
    // Serialize message field [gripper_opening_width]
    bufferOffset = _serializer.int32(obj.gripper_opening_width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspInput
    let len;
    let data = new GraspInput(null);
    // Deserialize message field [input_pc]
    data.input_pc = sensor_msgs.msg.PointCloud2.deserialize(buffer, bufferOffset);
    // Deserialize message field [goal_frame_id]
    data.goal_frame_id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [grasp_area_center]
    data.grasp_area_center = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [grasp_area_length_x]
    data.grasp_area_length_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [grasp_area_length_y]
    data.grasp_area_length_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max_calculation_time]
    data.max_calculation_time = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [show_only_best_grasp]
    data.show_only_best_grasp = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [threshold_grasp_evaluation]
    data.threshold_grasp_evaluation = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [approach_vector]
    data.approach_vector = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [gripper_opening_width]
    data.gripper_opening_width = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.PointCloud2.getMessageSize(object.input_pc);
    length += object.goal_frame_id.length;
    return length + 77;
  }

  static datatype() {
    // Returns string type for a message object
    return 'haf_grasping/GraspInput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7fc0ab7dae77f5f03563273dd280b0a3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    #Header header                        	# header for time/frame information
    sensor_msgs/PointCloud2 input_pc     	# defines the point cloud on which grasps should be calculated (objects)
    string goal_frame_id				 	# the frame_id to which the point cloud should be transformed before grasps are calculated
    geometry_msgs/Point grasp_area_center 	# center of the region where grasps are searched
    float32 grasp_area_length_x				# defines the length of the rectangle (in x direction (in m)) where grasps are searched (with center grasp_area_center)
    float32 grasp_area_length_y				# defines the length of the rectangle (in y direction (in m)) where grasps are searched (with center grasp_area_center)
    
    
    duration max_calculation_time			# maximal calculation time before grasp result is returned
    bool show_only_best_grasp				# If true, only the best grasp is shown in visualization
    int32 threshold_grasp_evaluation		# defines the threshold for return_first_grasp_over_th if it is set to true (otherwise it is ignored)
    
    geometry_msgs/Vector3 approach_vector	# defines the direction from where a grasp should be executed 
    int32 gripper_opening_width				# defines the factor (actually 1/factor) that is used for pre-grasp opening gripper width 
    
    #geometry_msgs/Vector3 scale_gripper	# Scale of the gripper in x and y direction if it deviates from a gripper of the size of a huMAN hand
    
    
    ================================================================================
    MSG: sensor_msgs/PointCloud2
    # This message holds a collection of N-dimensional points, which may
    # contain additional information such as normals, intensity, etc. The
    # point data is stored as a binary blob, its layout described by the
    # contents of the "fields" array.
    
    # The point cloud data may be organized 2d (image-like) or 1d
    # (unordered). Point clouds organized as 2d images may be produced by
    # camera depth sensors such as stereo or time-of-flight.
    
    # Time of sensor data acquisition, and the coordinate frame ID (for 3d
    # points).
    Header header
    
    # 2D structure of the point cloud. If the cloud is unordered, height is
    # 1 and width is the length of the point cloud.
    uint32 height
    uint32 width
    
    # Describes the channels and their layout in the binary data blob.
    PointField[] fields
    
    bool    is_bigendian # Is this data bigendian?
    uint32  point_step   # Length of a point in bytes
    uint32  row_step     # Length of a row in bytes
    uint8[] data         # Actual point data, size is (row_step*height)
    
    bool is_dense        # True if there are no invalid points
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    ================================================================================
    MSG: sensor_msgs/PointField
    # This message holds the description of one point entry in the
    # PointCloud2 message format.
    uint8 INT8    = 1
    uint8 UINT8   = 2
    uint8 INT16   = 3
    uint8 UINT16  = 4
    uint8 INT32   = 5
    uint8 UINT32  = 6
    uint8 FLOAT32 = 7
    uint8 FLOAT64 = 8
    
    string name      # Name of field
    uint32 offset    # Offset from start of point struct
    uint8  datatype  # Datatype enumeration, see above
    uint32 count     # How many elements in the field
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspInput(null);
    if (msg.input_pc !== undefined) {
      resolved.input_pc = sensor_msgs.msg.PointCloud2.Resolve(msg.input_pc)
    }
    else {
      resolved.input_pc = new sensor_msgs.msg.PointCloud2()
    }

    if (msg.goal_frame_id !== undefined) {
      resolved.goal_frame_id = msg.goal_frame_id;
    }
    else {
      resolved.goal_frame_id = ''
    }

    if (msg.grasp_area_center !== undefined) {
      resolved.grasp_area_center = geometry_msgs.msg.Point.Resolve(msg.grasp_area_center)
    }
    else {
      resolved.grasp_area_center = new geometry_msgs.msg.Point()
    }

    if (msg.grasp_area_length_x !== undefined) {
      resolved.grasp_area_length_x = msg.grasp_area_length_x;
    }
    else {
      resolved.grasp_area_length_x = 0.0
    }

    if (msg.grasp_area_length_y !== undefined) {
      resolved.grasp_area_length_y = msg.grasp_area_length_y;
    }
    else {
      resolved.grasp_area_length_y = 0.0
    }

    if (msg.max_calculation_time !== undefined) {
      resolved.max_calculation_time = msg.max_calculation_time;
    }
    else {
      resolved.max_calculation_time = {secs: 0, nsecs: 0}
    }

    if (msg.show_only_best_grasp !== undefined) {
      resolved.show_only_best_grasp = msg.show_only_best_grasp;
    }
    else {
      resolved.show_only_best_grasp = false
    }

    if (msg.threshold_grasp_evaluation !== undefined) {
      resolved.threshold_grasp_evaluation = msg.threshold_grasp_evaluation;
    }
    else {
      resolved.threshold_grasp_evaluation = 0
    }

    if (msg.approach_vector !== undefined) {
      resolved.approach_vector = geometry_msgs.msg.Vector3.Resolve(msg.approach_vector)
    }
    else {
      resolved.approach_vector = new geometry_msgs.msg.Vector3()
    }

    if (msg.gripper_opening_width !== undefined) {
      resolved.gripper_opening_width = msg.gripper_opening_width;
    }
    else {
      resolved.gripper_opening_width = 0
    }

    return resolved;
    }
};

module.exports = GraspInput;
