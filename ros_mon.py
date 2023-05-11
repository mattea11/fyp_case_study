#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, LaserScan, Image, CameraInfo
from control_msgs.msg import JointControllerState
from geometry_msgs.msg import PoseStamped, Twist
from cv_bridge import CvBridge
import numpy as np
import cv2
import json

class ros_mon:
    
    def get_latest_distance():
        rospy.init_node('rover_distance_node')
        data = rospy.wait_for_message('/merged_scan', LaserScan)

        dist = data.ranges
        dist = f"{dist:.3f}"

        my_dict = {'curr_distances': dist}
        json_speed = json.dumps(my_dict)
        return json_speed

    def get_latest_speed():
        rospy.init_node('rover_speed_node')
        data = rospy.wait_for_message('/curiosity_mars_rover/odom', Odometry)

        speed = data.twist.twist.linear.x
        speed = f"{speed:.6f}"

        my_dict = {'curr_speed': speed}
        json_speed = json.dumps(my_dict)
        return json_speed

    def get_latest_arm_horiz():  
        rospy.init_node('rover_horiz_angle_node')
        data = rospy.wait_for_message('/curiosity_mars_rover/mast_02_joint_position_controller/state', JointControllerState)

        angle = data.process_value
        angle = angle * 180.0 / 3.14

        my_dict = {'curr_horiz_angle': angle}
        json_angle = json.dumps(my_dict)
        return json_angle

    def get_latest_arm_vert(): 
        rospy.init_node('vert_angle_node')          
        data = rospy.wait_for_message('/curiosity_mars_rover/mast_cameras_joint_position_controller/state', JointControllerState)

        angle = data.process_value
        angle = angle

        my_dict = {'curr_vert_ang': angle}
        json_angle = json.dumps(my_dict)
        return json_angle
