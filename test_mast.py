import random
import rospy
import tf
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from tf.transformations import *

# class NavigationPublishAndWait:
    # def __init__(self):
def send_command():
    rospy.init_node('test_mast_node', anonymous=True)

    pub = rospy.Publisher('/curiosity_mars_rover/mast_cameras_joint_position_controller/command', Float64, queue_size=10) 
    # rospy.Subscriber('/curiosity_mars_rover/mast_cameras_joint_position_controller/state', JointControllerState, self.callback_result)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = 3.14
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        # rospy.sleep(1)
        # self.listener = tf.TransformListener()
        # self.rate = rospy.Rate(10)
        # self.result = False
        # # Initialise recorded positions as unlikely results (1km from origin)
        # self.final_x = 1000
        # self.final_y = 1000
        # self.final_rot = 10
        # self.speed = 0

    # def   send_goal(self, x, y, rot, speed):  
    #     # Send a simple navigation goal to the action server
    #     pose = PoseStamped()
    #     pose.header.frame_id = "odom"
    #     pose.header.stamp = rospy.Time.now()
    #     pose.pose.position.x = x
    #     pose.pose.position.y = y
    #     pose.pose.position.z = 0
    #     pose.pose.orientation.x = 0
    #     pose.pose.orientation.y = 0
    #     # Convert random rotation in radians to quaternion
    #     quaternion = quaternion_from_euler(0, 0, rot)
    #     pose.pose.orientation.z = quaternion[2]
    #     pose.pose.orientation.w = quaternion[3]
    #     self.pub.publish(pose)

    #     # Send a velocity command to control the speed of the robot
    #     vel_cmd = Twist()
    #     vel_cmd.linear.x = speed

    # def wait_for_result(self):
    #     # Wait for callback_result to be called
    #     while not self.result and not rospy.is_shutdown():
    #         self.rate.sleep()
    #     # Set the final recorded position of the rover after action server sends result
    #     self.final_pos, self.final_rot = self.listener.lookupTransform('odom', 'base_link', rospy.Time(0))
    #     self.final_rot = euler_from_quaternion(self.final_rot)

    # def callback_result(self, data):
    #     self.result = True

if __name__ == '__main__':

    try:
        send_command()
    except rospy.ROSInterruptException:
        pass
    # Instantiate NavigationPublishAndWait
    # tester = NavigationPublishAndWait()

    # # Send a random navigation goal and wait for result
    
    # random_x = round(random.uniform(-10, 10), 2) 
    # random_y = round(random.uniform(-10, 10), 2)
    # random_rot = round(random.uniform(-3.14, 3.14), 2)
    # speed = 0.5
    # tester.send_goal(random_x, random_y, random_rot, speed)
    # tester.wait_for_result()

    # # Print the final position and rotation of the robot
    # print("Final position: ({}, {})".format(tester.final_pos[0], tester.final_pos[1]))
    # print("Final rotation: {}".format(tester.final_rot[2]))
