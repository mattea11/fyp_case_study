#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    with open("ros_topic_data.txt", "a") as f:
        f.write(data.data + "\n")

def listener():
    rospy.init_node('listening_fronthaz_depth_points', anonymous=True)
    rospy.Subscriber("/curiosity_mars_rover/camera_fronthazcam/depth/points", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()