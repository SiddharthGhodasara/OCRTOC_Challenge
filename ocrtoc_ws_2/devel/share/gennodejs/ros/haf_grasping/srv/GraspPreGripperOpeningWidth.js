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

class GraspPreGripperOpeningWidthRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.gripper_opening_width = null;
    }
    else {
      if (initObj.hasOwnProperty('gripper_opening_width')) {
        this.gripper_opening_width = initObj.gripper_opening_width
      }
      else {
        this.gripper_opening_width = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspPreGripperOpeningWidthRequest
    // Serialize message field [gripper_opening_width]
    bufferOffset = _serializer.int32(obj.gripper_opening_width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspPreGripperOpeningWidthRequest
    let len;
    let data = new GraspPreGripperOpeningWidthRequest(null);
    // Deserialize message field [gripper_opening_width]
    data.gripper_opening_width = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspPreGripperOpeningWidthRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd0f2ffb7339463e86d9c2a177592739e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 gripper_opening_width			# factor f that is used for scaling point cloud to imitate pre-gripper opening width of 1/f
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspPreGripperOpeningWidthRequest(null);
    if (msg.gripper_opening_width !== undefined) {
      resolved.gripper_opening_width = msg.gripper_opening_width;
    }
    else {
      resolved.gripper_opening_width = 0
    }

    return resolved;
    }
};

class GraspPreGripperOpeningWidthResponse {
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
    // Serializes a message object of type GraspPreGripperOpeningWidthResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspPreGripperOpeningWidthResponse
    let len;
    let data = new GraspPreGripperOpeningWidthResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'haf_grasping/GraspPreGripperOpeningWidthResponse';
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
    const resolved = new GraspPreGripperOpeningWidthResponse(null);
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
  Request: GraspPreGripperOpeningWidthRequest,
  Response: GraspPreGripperOpeningWidthResponse,
  md5sum() { return '01233f977ab6b3bc3035826d00041c09'; },
  datatype() { return 'haf_grasping/GraspPreGripperOpeningWidth'; }
};
