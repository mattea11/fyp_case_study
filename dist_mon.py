#!/usr/bin/env python

# import rospy
# from sensor_msgs.msg import LaserScan

# def scan_callback(scan_data):
#     ranges = scan_data.ranges
#     print("Laser Scan Data:")
#     print("Number of ranges: ", len(ranges))
#     print("Ranges: ", ranges)

# if __name__ == '__main__':
#     rospy.init_node('scan_listener', anonymous=True)
#     rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
#     rospy.spin()

import rospy
from sensor_msgs.msg import LaserScan

def callback(scan_data):
    ranges = scan_data.ranges
    print("Laser Scan Data:")
    print("Number of ranges: ", len(ranges))
    print("Ranges: ", ranges)

def listener():
    # Initialize the node
    rospy.init_node('scan_listener', anonymous=True)

    # Subscribe to the topic
    rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, callback)

    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()