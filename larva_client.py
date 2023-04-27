import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from control_msgs.msg import JointControllerState
import json
import websocket

# Specify the WebSocket server URL
websocket_url = "ws://192.168.4.21:8080"
print('this is the ip ' + websocket_url)

# Connect to the WebSocket server
print('Connecting to server')
ws = websocket.create_connection(websocket_url)
print('Connected to Larva server successfully!')

ws.send("{\"msg\": \"Client attempting to connect\"}")
print('sent msg!!!')


# Callback function for sending JSON objects to the server
def send_data_to_larva(json_obj):
    ws.send(json_obj)
    print('Sent JSON object:', json_obj)

# Callback function for Odometry data
def odom_callback(data):
    lin_vel = data.twist.twist.linear.x

    # Create JSON object
    json_obj = json.dumps({"speed": lin_vel})

    # Send JSON object to server
    send_data_to_larva(json_obj)

# Callback function for LaserScan data
def scan_callback(scan_data):
    ranges = scan_data.ranges

    # Create JSON object
    json_obj = json.dumps({"dist": ranges})

    # Send JSON object to server
    send_data_to_larva(json_obj)

# Callback function for JointControllerState data
def arm_callback(data):
    arm_angel = data.process_value

    # Create JSON object
    json_obj = json.dumps({"mast_angle": arm_angel * 180.0 / 3.14})

    # Send JSON object to server
    send_data_to_larva(json_obj)

def listener():
    # Initialize the node
    rospy.init_node('data_collector', anonymous=True)

    # Subscribe to the topics
    rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback)
    rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
    rospy.Subscriber("/curiosity_mars_rover/arm_01_joint_position_controller/state", JointControllerState, arm_callback)

    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Close the WebSocket connection
        if ws:
            print('Closing connection')
            ws.close()





































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
    
#     json_obj = {"mast_angle": arm_angel}

#     mast_obj = json.dumps(json_obj)
#     print('mast object: ' + mast_obj)
#     return mast_obj

# def listener():
#     # Initialize the node
#     rospy.init_node('data_collector', anonymous=True)

#     # Subscribe to the topics
#     rospy.Subscriber("odom", Odometry, odom_callback)
#     rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
#     rospy.Subscriber("/curiosity_mars_rover/arm_01_joint_position_controller/state", JointControllerState, arm_callback)
    
#     # Spin until shutdown
#     rospy.spin()

# if __name__ == '__main__':
#     listener()
