import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from control_msgs.msg import JointControllerState
import json
import socket

HOST = "192.168.4.21"
PORT = 8080

# Create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send a message to the server
message = '{"mast_angle_vert": 0.00135051536338795}'
client_socket.sendall(message.encode())

# Receive a response from the server
data = client_socket.recv(1024)
print('Received from server: ', data.decode())


# Callback function for sending JSON objects to the server
def send_data_to_larva(json_obj):
    client_socket.sendall(json_obj.encode())
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
def arm_horiz_callback(data):
    arm_angel = data.process_value
    # Create JSON object
    json_obj = json.dumps({"mast_angle_horiz": arm_angel * 180.0 / 3.14})
    # Send JSON object to server
    send_data_to_larva(json_obj)

def arm_vert_callback(data):
    arm_angel = data.process_value
    # Create JSON object
    json_obj = json.dumps({"mast_angle_vert": arm_angel * 180.0 / 3.14})
    # Send JSON object to server
    send_data_to_larva(json_obj)

def listener():
    # Initialize the node
    rospy.init_node('data_collector', anonymous=True)

    # Subscribe to the topics
    rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback) #rostopic for rover speed
    # rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
    # rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_horiz_callback) #rostopic for camera horizontal turn
    # rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_vert_callback) #rostopic for camera horizontal turn

    # Spin until shutdown
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


    # finally:
    #     # Close the WebSocket connection
    #     if ws:
    #         print('Closing connection')
    #         ws.close()

