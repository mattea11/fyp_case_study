#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, Image, CameraInfo
from control_msgs.msg import JointControllerState
from cv_bridge import CvBridge
import numpy as np
import cv2
import json

class ros_monitoring:

def dist_callback(scan_data):
    ranges = scan_data.ranges
    # Create JSON object
    json_obj = json.dumps({"dist": ranges})
    return json_obj

def speed_callback(data):
    lin_vel = data.twist.twist.linear.x
    # Create JSON object
    json_obj = json.dumps({"speed": lin_vel})
    return json_obj

def arm_horiz_callback(data):
    arm_angel = data.process_value
    # Create JSON object
    json_obj = json.dumps({"mast_angle_horiz": arm_angel * 180.0 / 3.14})
    # Send JSON object to server
    return json_obj

def arm_vert_callback(data):
    arm_angel = data.process_value
    # Create JSON object
    json_obj = json.dumps({"mast_angle_vert": arm_angel * 180.0 / 3.14})
    # Send JSON object to server
    return json_obj

def depth_callback(msg):
    # Convert depth image to numpy array
    bridge = CvBridge()
    depth_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
    depth_array = np.array(depth_image, dtype=np.float32)

    # Get camera calibration parameters from camera info topic
    camera_info_topic = "/curiosity_mars_rover/camera_navcam/depth/camera_info"
    camera_info_msg = rospy.wait_for_message(camera_info_topic, CameraInfo)
    fx = camera_info_msg.K[0]
    fy = camera_info_msg.K[4]
    cx = camera_info_msg.K[2]
    cy = camera_info_msg.K[5]

    # Calculate distance to object
    object_pixel_x = 320  # Replace with actual pixel coordinates of object
    object_pixel_y = 240
    depth = depth_array[object_pixel_y, object_pixel_x]
    distance = depth / fx

    # Print distance to console
    rospy.loginfo("Distance to object: {} meters".format(distance))

def ros_mon_listener():
    # Initialize the node
    rospy.init_node('ros_monitor', anonymous=True)

    # rospy.Subscriber("/curiosity_mars_rover/camera_navcam/depth/image_raw", Image, depth_callback)

    # Subscribe to the topics to collect data
    # rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, speed_callback) #rostopic for rover speed
    # rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, dist_callback)
    rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_horiz_callback) #rostopic for camera horizontal turn
    rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_vert_callback) #rostopic for camera horizontal turn

    # Spin until shutdown
    rospy.spin()
