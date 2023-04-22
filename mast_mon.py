# get the mast angle
import rospy
from control_msgs.msg import JointControllerState

def callback(data):
    # Print the current position of the arm
    rospy.loginfo("Current arm position: %f", data.process_value)

def listener():
    # Initialize the node
    rospy.init_node('arm_position_listener', anonymous=True)

    # Subscribe to the topic
    rospy.Subscriber("/curiosity_mars_rover/arm_01_joint_position_controller/state", JointControllerState, callback)

    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()