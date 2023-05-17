#!/usr/bin/env python

from create_json import create_json
from ros_mon import ros_mon
import socket
import sys
import time


if __name__ == '__main__':  

    # start_client()
    HOST = "192.168.4.21"
    PORT = 8081

    # Create a TCP socket and connect to the server
    print('Waiting to connect to Larva Server')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print('Connected to the Larva server!')

        #create ndoe fro all monitors
        r = ros_mon()
        print("lol")

        # #testing mast prop
        # curr_data = r.get_latest_arm_vert()
        # change_data = create_json.change_vert(-1.03)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_arm_vert()
        # change_data = create_json.change_vert(1.03)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_arm_vert()
        # change_data = create_json.change_vert(0.03)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        
        # #testing speed prop
        # curr_data = r.get_latest_speed()
        # change_data = create_json.change_speed(3.0)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_speed()
        # change_data = create_json.change_speed(7.0)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        
        # curr_data = r.get_latest_speed()
        # change_data = create_json.change_speed(4.5)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_speed()
        # change_data = create_json.change_speed(3.5)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        
        #testing navigation prop
        curr_speed = r.get_latest_speed()
        curr_dist = r.get_latest_distance()
        change_nav = create_json.change_nav(0.9, 0 , 0.71, 0.71)
        change_speed = create_json.change_speed(3)
        to_send = create_json.merge_json(curr_speed, curr_dist)
        to_send = create_json.merge_json(to_send, change_speed)
        to_send = create_json.merge_json(to_send, change_nav)
        print("Sending command:\n ", to_send)
        create_json.send_data_to_larva(client_socket, to_send)
        print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        # #time.sleep(1)

        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(0.9, 0 , 0, 1)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        # #time.sleep(1)
        
        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(-0.9, 0 , 0.71, 0.71)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        # #time.sleep(1)
        
        # curr_data_nav = r.get_latest_distance()
        # curr_data_speed = r.get_latest_speed()
        # change_data_nav = create_json.change_nav(2, 0 , 0, 1)
        # to_send = create_json.merge_json(curr_data_nav, change_data_nav)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        # #time.sleep(1)
        
        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(2.5, 0 , 0.71, 0.71)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break
        # #time.sleep(1)

        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(2, 0 , 0.71, 0.71)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(2.9, 0 , 0, 1)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        # while True:
        #     data = client_socket.recv(1024)
        #     if "move on" in data.decode():
        #         print("Received message: ", data.decode())
        #         break

        # curr_data = r.get_latest_distance()
        # change_data = create_json.change_nav(2, 0 , 0.71, 0.71)
        # to_send = create_json.merge_json(curr_data, change_data)
        # print("Sending command:\n ", to_send)
        # create_json.send_data_to_larva(client_socket, to_send)
        # print('sent')

        while True:
            data = client_socket.recv(1024)
            if "move on" in data.decode():
                print("Received message: ", data.decode())
                break

        end_prog = create_json.create_gen_msg('end_program', -1)
        print('~~~ lol ~~~', end_prog)
        create_json.send_data_to_larva(client_socket, end_prog)
        sys.exit(0)
