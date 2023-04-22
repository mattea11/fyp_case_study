# import rospy
# from nav_msgs.msg import Odometry

# def odom_callback(data):
#     # Get linear velocity from odometry message
#     lin_vel = data.twist.twist.linear.x
#     print("Robot speed: ", lin_vel)

# if __name__ == '__main__':
#     rospy.init_node('speed_monitor')
#     rospy.Subscriber("/curiosity_mars_rover/ackermann_drive_controller/odom", Odometry, odom_callback)
#     rospy.spin()


#get the speed
# import rospy
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist

# def scan_callback(scan):
#     # Get the minimum non-zero range value from the scan data
#     valid_ranges = [range_val for range_val in scan.ranges if range_val > 0]
#     if valid_ranges:
#         min_range = min(valid_ranges)
#         rospy.loginfo("Distance to closest object: {} meters".format(min_range))
#     else:
#         rospy.loginfo("No objects detected")
    
#     rospy.loginfo("dist" + scan.ranges[360])

# rospy.init_node("distance_to_object")
# rospy.Subscriber("/curiosity_mars_rover/camera_fronthazcam/scan", LaserScan, scan_callback)
# rospy.spin()

#get the mast angle
# import rospy
# from control_msgs.msg import JointControllerState

# def callback(data):
#     # Print the current position of the arm
#     rospy.loginfo("Current arm position: %f", data.process_value)

# def listener():
#     # Initialize the node
#     rospy.init_node('arm_position_listener', anonymous=True)

#     # Subscribe to the topic
#     rospy.Subscriber("/curiosity_mars_rover/arm_01_joint_position_controller/state", JointControllerState, callback)

#     # Spin until shutdown
#     rospy.spin()

# if __name__ == '__main__':
#     listener()

# import socket

# HOST = 'localhost'
# PORT = 9090

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'hello!!')
# print('slayy')


import asyncio
import websockets
import json

# ROSBridge server URL and port
rosbridge_url = "ws://localhost:9090"

# This function sends a message to the ROSBridge server
async def send_to_rosbridge(message):
    async with websockets.connect(rosbridge_url) as websocket:
        await websocket.send(json.dumps(message))

# This function receives messages from the ROSBridge server and prints them
async def receive_from_rosbridge():
    async with websockets.connect(rosbridge_url) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received message from ROS: {message}")

# Set up asyncio event loop and tasks to run the send/receive functions
loop = asyncio.get_event_loop()
loop.create_task(send_to_rosbridge({"op": "subscribe", "topic": "/tf"}))
loop.create_task(receive_from_rosbridge())
loop.run_forever()