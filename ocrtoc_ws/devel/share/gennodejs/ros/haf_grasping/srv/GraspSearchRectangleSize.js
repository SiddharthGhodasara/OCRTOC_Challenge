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

class GraspSearchRectangleSizeRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grasp_search_size_x = null;
      this.grasp_search_size_y = null;
    }
    else {
      if (initObj.hasOwnProperty('grasp_search_size_x')) {
        this.grasp_search_size_x = initObj.grasp_search_size_x
      }
      else {
        this.grasp_search_size_x = 0;
      }
      if (initObj.hasOwnProperty('grasp_search_size_y')) {
        this.grasp_search_size_y = initObj.grasp_search_size_y
      }
      else {
        this.grasp_search_size_y = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspSearchRectangleSizeRequest
    // Serialize message field [grasp_search_size_x]
    bufferOffset = _serializer.int32(obj.grasp_search_size_x, buffer, bufferOffset);
    // Serialize message field [grasp_search_size_y]
    bufferOffset = _serializer.int32(obj.grasp_search_size_y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspSearchRectangleSizeRequest
    let len;
    let data = new GraspSearchRectangleSizeRequest(null);
    // Deserialize message field [grasp_search_size_x]
    data.grasp_search_size_x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [grasp_search_size_y]
    data.grasp_search_size_y = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspSearchRectangleSizeRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5e9aa228a0f1d0fd7362424bd5a57ae8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 grasp_search_size_x
    int32 grasp_search_size_y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspSearchRectangleSizeRequest(null);
    if (msg.grasp_search_size_x !== undefined) {
      resolved.grasp_search_size_x = msg.grasp_search_size_x;
    }
    else {
      resolved.grasp_search_size_x = 0
    }

    if (msg.grasp_search_size_y !== undefined) {
      resolved.grasp_search_size_y = msg.grasp_search_size_y;
    }
    else {
      resolved.grasp_search_size_y = 0
    }

    return resolved;
    }
};

class GraspSearchRectangleSizeResponse {
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
    // Serializes a message object of type GraspSearchRectangleSizeResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspSearchRectangleSizeResponse
    let len;
    let data = new GraspSearchRectangleSizeResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspSearchRectangleSizeResponse';
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
    const resolved = new GraspSearchRectangleSizeResponse(null);
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
  Request: GraspSearchRectangleSizeRequest,
  Response: GraspSearchRectangleSizeResponse,
  md5sum() { return '10248c1006719d0893af769fe3ad61ba'; },
  datatype() { return 'haf_grasping/GraspSearchRectangleSize'; }
};
