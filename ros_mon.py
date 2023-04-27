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
    # rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback)
    # rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
    # rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_callback) #horizontal turn ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_callback) vertical ~~~~~~~~~~~~~~~~~~~~~~

    
    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()





# import rospy
# import numpy as np
# from sensor_msgs.msg import Image, CameraInfo
# from cv_bridge import CvBridge
# import cv2

# class NavcamDistanceEstimator:
#     def __init__(self):
#         rospy.init_node('navcam_distance_estimator')
#         self.bridge = CvBridge()
#         self.left_image = None
#         self.right_image = None
#         self.left_camera_info = None
#         self.right_camera_info = None
#         self.focal_length = None
#         self.baseline = None

#         # Subscribe to the image_raw topics of the left and right cameras
#         self.sub_left = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/image_raw', Image, self.left_callback)
#         self.sub_right = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/right/image_raw', Image, self.right_callback)

#         # Subscribe to the camera_info topics of the left and right cameras
#         self.sub_left_info = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/camera_info', CameraInfo, self.left_info_callback)
#         self.sub_right_info = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/camera_info', CameraInfo, self.right_info_callback)

#     def left_callback(self, msg):
#         self.left_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

#     def right_callback(self, msg):
#         self.right_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

#     def left_info_callback(self, msg):
#         self.left_camera_info = msg
#         if self.right_camera_info is not None:
#             self.calculate_baseline_and_focal_length()

#     def right_info_callback(self, msg):
#         self.right_camera_info = msg
#         if self.left_camera_info is not None:
#             self.calculate_baseline_and_focal_length()

#     def calculate_baseline_and_focal_length(self):
#         left_fx = self.left_camera_info.K[0]
#         right_fx = self.right_camera_info.K[0]
#         baseline = abs(self.left_camera_info.P[3] / left_fx - self.right_camera_info.P[3] / right_fx)
#         self.baseline = baseline
#         self.focal_length = (left_fx + right_fx) / 2

#     def calculate_distance(self):
#         if self.left_image is None or self.right_image is None or self.focal_length is None or self.baseline is None:
#             return None

#         # Convert images to grayscale
#         left_gray = cv2.cvtColor(self.left_image, cv2.COLOR_BGR2GRAY)
#         right_gray = cv2.cvtColor(self.right_image, cv2.COLOR_BGR2GRAY)

#         # Perform block matching algorithm
#         stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
#         disparity = stereo.compute(left_gray, right_gray)

#         # Calculate depth from disparity
#         depth = self.focal_length * self.baseline / disparity

#         # Find minimum non-zero depth value
#         min_depth = np.min(depth[depth > 0])

#         # Calculate distance from minimum depth value
#         distance = min_depth

#         return distance

# if __name__ == '__main__':
#     estimator = NavcamDistanceEstimator()
#     rate = rospy.Rate(10) # 10 Hz

#     while not rospy.is_shutdown():
#         distance = estimator.calculate_distance()
#         if distance is not None:
#             rospy.loginfo('Distance: %f', distance)
#         rate.sleep()
