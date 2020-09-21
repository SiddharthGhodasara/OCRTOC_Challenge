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
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class GraspOutput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.eval = null;
      this.graspPoint1 = null;
      this.graspPoint2 = null;
      this.averagedGraspPoint = null;
      this.approachVector = null;
      this.roll = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('eval')) {
        this.eval = initObj.eval
      }
      else {
        this.eval = 0;
      }
      if (initObj.hasOwnProperty('graspPoint1')) {
        this.graspPoint1 = initObj.graspPoint1
      }
      else {
        this.graspPoint1 = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('graspPoint2')) {
        this.graspPoint2 = initObj.graspPoint2
      }
      else {
        this.graspPoint2 = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('averagedGraspPoint')) {
        this.averagedGraspPoint = initObj.averagedGraspPoint
      }
      else {
        this.averagedGraspPoint = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('approachVector')) {
        this.approachVector = initObj.approachVector
      }
      else {
        this.approachVector = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspOutput
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [eval]
    bufferOffset = _serializer.int32(obj.eval, buffer, bufferOffset);
    // Serialize message field [graspPoint1]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.graspPoint1, buffer, bufferOffset);
    // Serialize message field [graspPoint2]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.graspPoint2, buffer, bufferOffset);
    // Serialize message field [averagedGraspPoint]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.averagedGraspPoint, buffer, bufferOffset);
    // Serialize message field [approachVector]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.approachVector, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float32(obj.roll, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspOutput
    let len;
    let data = new GraspOutput(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [eval]
    data.eval = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [graspPoint1]
    data.graspPoint1 = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [graspPoint2]
    data.graspPoint2 = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [averagedGraspPoint]
    data.averagedGraspPoint = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [approachVector]
    data.approachVector = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 104;
  }

  static datatype() {
    // Returns string type for a message object
    return 'haf_grasping/GraspOutput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5d81f8c795c680629cc920340e4f0008';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    int32 eval
    geometry_msgs/Point graspPoint1
    geometry_msgs/Point graspPoint2
    geometry_msgs/Point averagedGraspPoint
    geometry_msgs/Vector3 approachVector
    float32 roll # radians
    
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
    const resolved = new GraspOutput(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.eval !== undefined) {
      resolved.eval = msg.eval;
    }
    else {
      resolved.eval = 0
    }

    if (msg.graspPoint1 !== undefined) {
      resolved.graspPoint1 = geometry_msgs.msg.Point.Resolve(msg.graspPoint1)
    }
    else {
      resolved.graspPoint1 = new geometry_msgs.msg.Point()
    }

    if (msg.graspPoint2 !== undefined) {
      resolved.graspPoint2 = geometry_msgs.msg.Point.Resolve(msg.graspPoint2)
    }
    else {
      resolved.graspPoint2 = new geometry_msgs.msg.Point()
    }

    if (msg.averagedGraspPoint !== undefined) {
      resolved.averagedGraspPoint = geometry_msgs.msg.Point.Resolve(msg.averagedGraspPoint)
    }
    else {
      resolved.averagedGraspPoint = new geometry_msgs.msg.Point()
    }

    if (msg.approachVector !== undefined) {
      resolved.approachVector = geometry_msgs.msg.Vector3.Resolve(msg.approachVector)
    }
    else {
      resolved.approachVector = new geometry_msgs.msg.Vector3()
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    return resolved;
    }
};

module.exports = GraspOutput;
