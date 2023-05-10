#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, Image, CameraInfo
from control_msgs.msg import JointControllerState
from geometry_msgs.msg import PoseStamped, Twist
from cv_bridge import CvBridge
import numpy as np
import cv2
import json

class ros_mon:

    def get_obj_orient(): # fix !!!!!!!!!!!!!
        def callback(scan_data):
            cd = scan_data.ranges
            return cd
        curr_dist = rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, callback)
        return curr_dist












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
        angle = angle #* 180.0 / 3.14

        my_dict = {'curr_vert_ang': angle}
        json_angle = json.dumps(my_dict)
        return json_angle
