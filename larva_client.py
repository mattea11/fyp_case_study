import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from control_msgs.msg import JointControllerState
import json
import socket

class larva_client:

    def start_client():
        HOST = "192.168.4.21"
        PORT = 8080

        # Create a TCP socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        # Receive a response from the server
        data = client_socket.recv(1024)
        print('Received from server: ', data.decode())

    def merge_json(json1, json2):
        merged_json = json.loads(json1)
        merged_json.update(json.loads(json2))
        return json.dumps(merged_json)

    # Callback function for sending JSON objects to the server
    def send_data_to_larva(client_socket, json_obj):
        client_socket.sendall(json_obj.encode())
        print('Sent JSON object:', json_obj)

    def listener():
        # Initialize the node
        rospy.init_node('data_collector', anonymous=True)

        # Subscribe to the topics
        rospy.Subscriber("/curiosity_mars_rover/odom", Odometry, odom_callback) #rostopic for rover speed
        rospy.Subscriber('/curiosity_mars_rover/camera_fronthazcam/scan', LaserScan, scan_callback)
        rospy.Subscriber("/curiosity_mars_rover/mast_02_joint_position_controller/state", JointControllerState, arm_horiz_callback) #rostopic for camera horizontal turn
        rospy.Subscriber("/curiosity_mars_rover/mast_cameras_joint_position_controller/state", JointControllerState, arm_vert_callback) #rostopic for camera horizontal turn

        # Spin until shutdown
        rospy.spin()
