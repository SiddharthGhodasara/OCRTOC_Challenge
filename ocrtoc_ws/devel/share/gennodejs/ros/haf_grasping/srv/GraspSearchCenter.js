// Auto-generated. Do not edit!

// (in-package haf_grasping.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class GraspSearchCenterRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.graspsearchcenter = null;
    }
    else {
      if (initObj.hasOwnProperty('graspsearchcenter')) {
        this.graspsearchcenter = initObj.graspsearchcenter
      }
      else {
        this.graspsearchcenter = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspSearchCenterRequest
    // Serialize message field [graspsearchcenter]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.graspsearchcenter, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspSearchCenterRequest
    let len;
    let data = new GraspSearchCenterRequest(null);
    // Deserialize message field [graspsearchcenter]
    data.graspsearchcenter = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspSearchCenterRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ea95ef8571fb59e1b8121fdcd68963c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Point graspsearchcenter
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
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
    const resolved = new GraspSearchCenterRequest(null);
    if (msg.graspsearchcenter !== undefined) {
      resolved.graspsearchcenter = geometry_msgs.msg.Point.Resolve(msg.graspsearchcenter)
    }
    else {
      resolved.graspsearchcenter = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

class GraspSearchCenterResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspSearchCenterResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspSearchCenterResponse
    let len;
    let data = new GraspSearchCenterResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspSearchCenterResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool result
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspSearchCenterResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: GraspSearchCenterRequest,
  Response: GraspSearchCenterResponse,
  md5sum() { return '2e7151a3ec270e58847862555bffd4c4'; },
  datatype() { return 'haf_grasping/GraspSearchCenter'; }
};
