#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionResult

def nav_callback(data):
    rospy.logdebug(rospy.get_caller_id() + "Received message: %s", data)
    rospy.loginfo(rospy.get_caller_id() + "Processing message result: %s", data.result)

def nav_move_listener():
    rospy.init_node('result_subscriber', anonymous=True)

    rospy.Subscriber("/move_base/result", MoveBaseActionResult, nav_callback)

    rospy.spin()

if __name__ == '__main__':
    nav_move_listener()

# from create_json import create_json
# from ros_mon import ros_mon

# import socket
# import json
# import time


# if __name__ == '__main__':  

#     # start_client()
#     HOST = "192.168.4.21"
#     PORT = 8080

#     # Create a TCP socket and connect to the server
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
#     print('connected to the Larva server!')

#     # send command and check validity
#     curr_data = ros_mon.get_latest_arm_vert()
#     print("test curr data: ", curr_data)
#     change_data = create_json.change_vert(-1.03)
#     to_send = create_json.merge_json(curr_data, change_data)
#     print("sending command: ", to_send)
#     create_json.send_data_to_larva(client_socket, to_send)
#     print('sent11111111111111')

#     #do not send next command before larva says so
#     while True:
#         data = client_socket.recv(1024)
#         if "move on" in data.decode():
#             print("Received message: ", data.decode())
#             break

#     curr_data = ros_mon.get_latest_arm_vert()
#     # print("test curr data: ", curr_data)
#     change_data = create_json.change_vert(1)
#     to_send = create_json.merge_json(curr_data, change_data)
#     print("sending command: ", to_send)
#     create_json.send_data_to_larva(client_socket, to_send)
#     print('sent11111111111111')

#     while True:
#         data = client_socket.recv(1024)
#         if "move on" in data.decode():
#             print("Received message: ", data.decode())
#             break

#     end_prog = create_json.create_gen_msg('end program', -1)
#     print(end_prog)
#     create_json.send_data_to_larva(client_socket, to_send)
#     print('bye')
#     ##########

#     #send command and check validity
#     # curr_data = ros_mon.get_latest_speed()
#     # # print("test curr data: ", curr_data)
#     # change_data = create_json.change_speed(27)
#     # to_send = create_json.merge_json(curr_data, change_data)
#     # print("sending command: ", to_send)
#     # create_json.send_data_to_larva(client_socket, to_send)
#     # print('sent11111111111111')

#     # #do not send next command before larva says so
#     # while True:
#     #     data = client_socket.recv(1024)
#     #     if "move on" in data.decode():
#     #         print("Received message: ", data.decode())
#     #         break

#     # curr_data = ros_mon.get_latest_speed()
#     # change_data = create_json.change_speed(0.4)
#     # to_send = create_json.merge_json(curr_data, change_data)
#     # print("sending command: ", to_send)
#     # create_json.send_data_to_larva(client_socket, to_send)
#     # print('sent22222222222222222222222222')

#     # end_prog = create_json.create_gen_msg('end program', -1)
#     # print(end_prog)
#     # create_json.send_data_to_larva(client_socket, to_send)
#     # print('bye')