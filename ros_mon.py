#!/usr/bin/env python

# import rospy
# from geometry_msgs.msg import Twist

# def vel_callback(msg):
#     speed = msg.linear.x
#     print(f"currently:\tspeed {speed:.2f}")

# def listener():
#     print('init node')
#     rospy.init_node('speed_monitor', anonymous=True)
#     print('subscribing')
#     rospy.Subscriber("/curiosity_mars_rover/ackermann_drive_controller/cmd_vel", Twist, vel_callback)
#     rospy.spin()

# if __name__ == '__main__':
#     print('2hello')
#     listener()







import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from control_msgs.msg import JointControllerState
import json

# Global variables to store data
lin_vel = 0.0
ranges = []
arm_angel = 0.0

def odom_callback(data):
    global lin_vel
    lin_vel = data.twist.twist.linear.x

    json_obj = {"speed": lin_vel}

    speed_obj = json.dumps(json_obj)
    print('speed object: ' + speed_obj)
    return speed_obj

def scan_callback(scan_data):
    global ranges
    ranges = scan_data.ranges

    # change depending on what i plan on using
    json_obj = {"dist": ranges}

    dist_obj = json.dumps(json_obj)
    print('dist object: ' + dist_obj)
    return dist_obj

def arm_callback(data):
    global arm_angel
    arm_angel = data.process_value
    
    json_obj = {"mast_angle": arm_angel * 180.0 / 3.14}

    mast_obj = json.dumps(json_obj)
    print('mast object: ' + mast_obj)
    return mast_obj

def listener():
    # Initialize the node
    rospy.init_node('data_collector', anonymous=True)

    # Subscribe to the topics
    rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback)
    # rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
    # rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_callback) #horizontal turn ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_callback) vertical ~~~~~~~~~~~~~~~~~~~~~~

    
    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()