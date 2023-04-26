import rospy
from nav_msgs.msg import Odometry

def callback(data):
    lin_vel = data.twist.twist.linear.x
    print("Robot speed: ", lin_vel)

def listener():
    # Initialize the node
    rospy.init_node('speed_monitor', anonymous=True)
    # Subscribe to the topic
    rospy.Subscriber("odom", Odometry, callback)
    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()