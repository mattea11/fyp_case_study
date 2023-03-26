# import sys

# def lol():
#     try :
#         with open('./src/curiosity_mars_rover_navigation/scripts/move_rover.txt', 'r') as path_to_take:
#             for command in path_to_take:
#                 print(command.strip())
#     except FileNotFoundError:
#         print("Error: file not found!")
#         sys.exit(1)


# lol()

#!/usr/bin/env python3

# Navigation tester that sends random goals, waits for a result message and
# compares the final rover position with the goal position originally sent.
  
# Decorator for asynchronous testing, borrowed from:
# https://stackoverflow.com/questions/23033939/how-to-test-python-3-4-asyncio-code


import random
import rospy
import tf
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionResult
from tf.transformations import *

# ./src/ros_monitoring/src/obsticle_dist.py

class NavigationPublishAndWait:
    def __init__(self):
        self.pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        rospy.Subscriber('/move_base/result', MoveBaseActionResult, self.callback_result)
        rospy.init_node('test_nav_node', anonymous=True)
        rospy.sleep(1)
        self.listener = tf.TransformListener()
        self.rate = rospy.Rate(10)
        self.result = False
        # Initialise recorded positions as unlikely results (1km from origin)
        self.final_x = 1000
        self.final_y = 1000
        self.final_rot = 10

    def send_goal(self, x, y, rot):
        # Send a simple navigation goal to the action server
        pose = PoseStamped()
        pose.header.frame_id = "odom"
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0
        pose.pose.orientation.x = 0
        pose.pose.orientation.y = 0
        # Convert random rotation in radians to quaternion
        quaternion = quaternion_from_euler(0, 0, rot)
        pose.pose.orientation.z = quaternion[2]
        pose.pose.orientation.w = quaternion[3]
        self.pub.publish(pose)

    def wait_for_result(self):
        # Wait for callback_result to be called
        while not self.result and not rospy.is_shutdown():
            self.rate.sleep()
        # Set the final recorded position of the rover after action server sends result
        self.final_pos, self.final_rot = self.listener.lookupTransform('odom', 'base_link', rospy.Time(0))
        self.final_rot = euler_from_quaternion(self.final_rot)

    def callback_result(self, data):
        self.result = True

if __name__ == '__main__':
    # Instantiate NavigationPublishAndWait
    tester = NavigationPublishAndWait()

    # Send a random navigation goal and wait for result
    random_x = round(random.uniform(-10, 10), 2) 
    random_y = round(random.uniform(-10, 10), 2)
    random_rot = round(random.uniform(-3.14, 3.14), 2)
    tester.send_goal(random_x, random_y, random_rot)
    tester.wait_for_result()

    # Print the final position and rotation of the robot
    print("Final position: ({}, {})".format(tester.final_pos[0], tester.final_pos[1]))
    print("Final rotation: {}".format(tester.final_rot[2]))

