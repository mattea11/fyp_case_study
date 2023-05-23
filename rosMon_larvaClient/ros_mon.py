#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, LaserScan
from control_msgs.msg import JointControllerState
import json

class ros_mon:
    def __init__(self):
        rospy.init_node('rover_mon_node', anonymous=True)


    #each of the following functions collects data for their respective property at the time and create a json object of the information
    def get_latest_distance(self):
        data = rospy.wait_for_message('/merged_scan', LaserScan)

        dist = data.ranges
        smallest = min(dist)
        smallest = f"{smallest:.2f}"
        my_dict = {'curr_distances': smallest}
        json_speed = json.dumps(my_dict)

        return json_speed

    def get_latest_speed(self):
        data = rospy.wait_for_message('/curiosity_mars_rover/odom', Odometry)

        speed = data.twist.twist.linear.x
        speed = f"{speed:.2f}"

        my_dict = {'curr_speed': speed}
        json_speed = json.dumps(my_dict)

        return json_speed

    def get_latest_arm_vert(self):        
        data = rospy.wait_for_message('/curiosity_mars_rover/mast_cameras_joint_position_controller/state', JointControllerState)

        angle = data.process_value
        angle = f"{angle:.2f}"

        my_dict = {'curr_vert_ang': angle}
        json_angle = json.dumps(my_dict)

        return json_angle
