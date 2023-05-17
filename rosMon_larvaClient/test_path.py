import random
import rospy
import tf
from geometry_msgs.msg import PoseStamped, Twist
from move_base_msgs.msg import MoveBaseActionResult

from tf.transformations import *

class NavigationPublishAndWait:
    def __init__(self): 
        self.pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10) 
        # pub = rospy.Publisher('/curiosity_mars_rover/ackermann_drive_controller/cmd_vel', Twist, queue_size=10)
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
        self.speed = 0

    def   send_goal(self, x, y, rot, speed):  
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

        # Send a velocity command to control the speed of the robot
        vel_cmd = Twist()
        vel_cmd.linear.x = speed

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
    speed = 0.5
    print('x: ', random_x)
    print('y: ', random_y)
    print('rot: ', random_rot)

    tester.send_goal(random_x, random_y, random_rot, speed)
    print('hello')
    tester.wait_for_result()
    print('done')

    # Print the final position and rotation of the robot
    print("Final position: ({}, {})".format(tester.final_pos[0], tester.final_pos[1]))
    print("Final rotation: {}".format(tester.final_rot[2]))
