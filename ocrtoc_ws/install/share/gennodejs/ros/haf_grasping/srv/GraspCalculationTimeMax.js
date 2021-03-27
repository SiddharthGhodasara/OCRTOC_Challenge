// Auto-generated. Do not edit!

// (in-package haf_grasping.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class GraspCalculationTimeMaxRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.max_calculation_time = null;
    }
    else {
      if (initObj.hasOwnProperty('max_calculation_time')) {
        this.max_calculation_time = initObj.max_calculation_time
      }
      else {
        this.max_calculation_time = {secs: 0, nsecs: 0};
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspCalculationTimeMaxRequest
    // Serialize message field [max_calculation_time]
    bufferOffset = _serializer.duration(obj.max_calculation_time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspCalculationTimeMaxRequest
    let len;
    let data = new GraspCalculationTimeMaxRequest(null);
    // Deserialize message field [max_calculation_time]
    data.max_calculation_time = _deserializer.duration(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspCalculationTimeMaxRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '08b29bcfc2f5ed2f5016420098e04b4c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    duration max_calculation_time			# maximal calculation time before grasp result is returned
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspCalculationTimeMaxRequest(null);
    if (msg.max_calculation_time !== undefined) {
      resolved.max_calculation_time = msg.max_calculation_time;
    }
    else {
      resolved.max_calculation_time = {secs: 0, nsecs: 0}
    }

    return resolved;
    }
};

class GraspCalculationTimeMaxResponse {
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
    // Serializes a message object of type GraspCalculationTimeMaxResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspCalculationTimeMaxResponse
    let len;
    let data = new GraspCalculationTimeMaxResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspCalculationTimeMaxResponse';
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
    const resolved = new GraspCalculationTimeMaxResponse(null);
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
  Request: GraspCalculationTimeMaxRequest,
  Response: GraspCalculationTimeMaxResponse,
  md5sum() { return 'fe39c4e255168ec5afaa585fcfbd448f'; },
  datatype() { return 'haf_grasping/GraspCalculationTimeMax'; }
};
