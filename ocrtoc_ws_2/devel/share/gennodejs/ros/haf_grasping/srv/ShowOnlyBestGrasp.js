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

class ShowOnlyBestGraspRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.show_only_best_grasp = null;
    }
    else {
      if (initObj.hasOwnProperty('show_only_best_grasp')) {
        this.show_only_best_grasp = initObj.show_only_best_grasp
      }
      else {
        this.show_only_best_grasp = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ShowOnlyBestGraspRequest
    // Serialize message field [show_only_best_grasp]
    bufferOffset = _serializer.bool(obj.show_only_best_grasp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ShowOnlyBestGraspRequest
    let len;
    let data = new ShowOnlyBestGraspRequest(null);
    // Deserialize message field [show_only_best_grasp]
    data.show_only_best_grasp = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/ShowOnlyBestGraspRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2884e314840573d98e3fd64b18c919d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool show_only_best_grasp			# ShowOnlyBestGrasp: defines if only the best grasp should be visualized
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ShowOnlyBestGraspRequest(null);
    if (msg.show_only_best_grasp !== undefined) {
      resolved.show_only_best_grasp = msg.show_only_best_grasp;
    }
    else {
      resolved.show_only_best_grasp = false
    }

    return resolved;
    }
};

class ShowOnlyBestGraspResponse {
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
    // Serializes a message object of type ShowOnlyBestGraspResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ShowOnlyBestGraspResponse
    let len;
    let data = new ShowOnlyBestGraspResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/ShowOnlyBestGraspResponse';
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
    const resolved = new ShowOnlyBestGraspResponse(null);
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
  Request: ShowOnlyBestGraspRequest,
  Response: ShowOnlyBestGraspResponse,
  md5sum() { return 'c13d71448b4276a64c7f5417c0cd390a'; },
  datatype() { return 'haf_grasping/ShowOnlyBestGrasp'; }
};
