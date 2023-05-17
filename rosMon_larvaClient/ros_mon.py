#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, LaserScan
from control_msgs.msg import JointControllerState
import json

class ros_mon:
    def __init__(self):
        rospy.init_node('rover_mon_node', anonymous=True)


    #each of tehf ollowing functions collects data for their respective property at teh tiem and create a json object of the information
    def get_latest_distance(self):
        # if not rospy.core.is_initialized(): 
        # rospy.init_node('rover_distance_node', anonymous=True)
        data = rospy.wait_for_message('/merged_scan', LaserScan)
        print(1)

        dist = data.ranges
        smallest = min(dist)
        smallest = f"{smallest:.3f}"
        print(2)
        my_dict = {'curr_distances': smallest}
        json_speed = json.dumps(my_dict)

        # rospy.signal_shutdown("Finished getting latest distance.")
        return json_speed

    def get_latest_speed(self):
        # if not rospy.core.is_initialized():
        # rospy.init_node('rover_speed_node', anonymous=True)
        data = rospy.wait_for_message('/curiosity_mars_rover/odom', Odometry)

        speed = data.twist.twist.linear.x
        speed = f"{speed:.6f}"

        my_dict = {'curr_speed': speed}
        json_speed = json.dumps(my_dict)

        # rospy.signal_shutdown("Finished getting latest speed.")
        return json_speed

    def get_latest_arm_vert(self): 
        # if not rospy.core.is_initialized():
        # rospy.init_node('vert_angle_node', anonymous=True)          
        data = rospy.wait_for_message('/curiosity_mars_rover/mast_cameras_joint_position_controller/state', JointControllerState)

        angle = data.process_value
        angle = angle

        my_dict = {'curr_vert_ang': angle}
        json_angle = json.dumps(my_dict)

        # rospy.signal_shutdown("Finished getting latest angle.")
        return json_angle
