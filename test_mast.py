import random
import rospy
import tf
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from tf.transformations import *

# def vert_command():


def send_command():
    rospy.init_node('test_mast_node', anonymous=True)

    pub_vert = rospy.Publisher('/curiosity_mars_rover/mast_cameras_joint_position_controller/command', Float64, queue_size=10) # for vert angle
    pub_horiz = rospy.Publisher('/curiosity_mars_rover/mast_02_joint_position_controller/command', Float64, queue_size=10) # for horiz angle
    # pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10) for navigation  
    # pub = rospy.Publisher('/curiosity_mars_rover/ackermann_drive_controller/cmd_vel', Twist, queue_size=10) for speed

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        position = -0.3
        rospy.loginfo(position)
        pub_vert.publish(position)

        position = -0.5
        rospy.loginfo(position)
        pub_vert.publish(position)

        position = 0.9
        rospy.loginfo(position)
        pub_vert.publish(position)

        position = -0.5
        rospy.loginfo(position)
        pub_horiz.publish(position)

        position = 0.5
        rospy.loginfo(position)
        pub_horiz.publish(position)

        rate.sleep()
        # rospy.signal_shutdown("Test simulation has finished !")



if __name__ == '__main__':

    try:
        send_command()
    except rospy.ROSInterruptException:
        pass
