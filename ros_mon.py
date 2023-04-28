# import rospy
# from nav_msgs.msg import Odometry
# from sensor_msgs.msg import LaserScan
# from control_msgs.msg import JointControllerState
# import json

# # Global variables to store data
# lin_vel = 0.0
# ranges = []
# arm_angel = 0.0

# def odom_callback(data):
#     global lin_vel
#     lin_vel = data.twist.twist.linear.x

#     json_obj = {"speed": lin_vel}

#     speed_obj = json.dumps(json_obj)
#     print('speed object: ' + speed_obj)
#     return speed_obj

# def scan_callback(scan_data):
#     global ranges
#     ranges = scan_data.ranges

#     # change depending on what i plan on using
#     json_obj = {"dist": ranges}

#     dist_obj = json.dumps(json_obj)
#     print('dist object: ' + dist_obj)
#     return dist_obj

# def arm_callback(data):
#     global arm_angel
#     arm_angel = data.process_value
    
#     json_obj = {"mast_angle": arm_angel * 180.0 / 3.14}

#     mast_obj = json.dumps(json_obj)
#     print('mast object: ' + mast_obj)
#     return mast_obj

# def listener():
#     # Initialize the node
#     rospy.init_node('data_collector', anonymous=True)

#     # Subscribe to the topics
#     # rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback)
#     # rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
#     # rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_callback) #horizontal turn ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     # rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_callback) vertical ~~~~~~~~~~~~~~~~~~~~~~

    
#     # Spin until shutdown
#     rospy.spin()

# if __name__ == '__main__':
#     listener()


#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo

class StereoDepth:
    def __init__(self):
        rospy.init_node('stereo_depth', anonymous=True)
        
        self.bridge = CvBridge()
        
        # Subscribe to the left and right camera topics
        self.left_image_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/image_raw', Image, self.left_image_callback)
        self.left_info_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/camera_info', CameraInfo, self.left_info_callback)
        self.right_image_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/right/image_raw', Image, self.right_image_callback)
        self.right_info_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/right/camera_info', CameraInfo, self.right_info_callback)
        
        self.fx, self.fy, self.cx, self.cy = None, None, None, None 
        self.left_image, self.right_image = None, None
        
        self.depth_scale = 0.001  # Conversion factor for disparity to depth (1 pixel = 1mm at 1 meter)
        
    def left_image_callback(self, msg):
        try:
            self.left_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
    
    def left_info_callback(self, msg):
        self.fx = msg.K[0]
        self.fy = msg.K[4]
        self.cx = msg.K[2]
        self.cy = msg.K[5]
        print(msg.K[0] ,msg.K[4] ,msg.K[2] ,msg.K[5])
        
    def right_image_callback(self, msg):
        try:
            print('pls?')
            self.right_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
    
    def right_info_callback(self, msg):
        pass
    
    def calculate_depth(self):
        if self.left_image is not None and self.right_image is not None:
            # Convert images to grayscale
            left_gray = cv2.cvtColor(self.left_image, cv2.COLOR_BGR2GRAY)
            right_gray = cv2.cvtColor(self.right_image, cv2.COLOR_BGR2GRAY)
            
            # Compute disparity map
            stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
            disparity = stereo.compute(left_gray, right_gray)
            
            # Compute depth map
            depth = self.fx * self.fy / (disparity + 0.0001) * self.depth_scale
            
            # Calculate distance to object at center of image
            x = int(self.cx)
            y = int(self.cy)
            distance = depth[y, x]
            
            rospy.loginfo('Distance to object: {:.2f} meters'.format(distance))
            
    def run(self):
        print('bef rate')
        rate = rospy.Rate(10)  # Hz
        print('after rate')
        while not rospy.is_shutdown():
            print('bef calc depth')
            self.calculate_depth()
            print('after calc depth')
            rate.sleep()

if __name__ == '__main__':
    try:
        print('lol')
        sd = StereoDepth()
        print('lol2')
        sd.run()
        print('lol3')
    except rospy.ROSInterruptException:
        pass
