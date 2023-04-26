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
    print("Robot speed: ", lin_vel)
    return lin_vel

def scan_callback(scan_data):
    global ranges
    ranges = scan_data.ranges
    print("Laser Scan Data:")
    print("Number of ranges: ", len(ranges))
    print("Ranges: ", ranges)

def arm_callback(data):
    global arm_angel
    arm_angel = data.process_value
    rospy.loginfo("Current arm position: %f", arm_angel)
    return arm_angel

def create_json_object():
    global lin_vel, ranges, arm_position
    # Create a dictionary object
    data_dict = {
        "lin_vel": lin_vel,
        "ranges": ranges,
        "arm_angel": arm_angel
    }
    # Convert the dictionary to JSON
    json_data = json.dumps(data_dict)
    print("JSON Object:", json_data)
    # Call another function to send the JSON data to another part of the code

def listener():
    # Initialize the node
    rospy.init_node('data_collector', anonymous=True)
    # Subscribe to the topics
    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
    rospy.Subscriber("/curiosity_mars_rover/arm_01_joint_position_controller/state", JointControllerState, arm_callback)
    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()
