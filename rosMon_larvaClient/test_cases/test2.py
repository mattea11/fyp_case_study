#!/usr/bin/env python

from create_json import create_json
from ros_mon import ros_mon
import socket
import sys
import json
import time


if __name__ == '__main__':  

    HOST = "192.168.4.21"
    PORT = 8081

    # Create a TCP socket and connect to the server
    print('Waiting to connect to Larva Server')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print('Connected to the Larva server!')
        
        with open('./command_validation_time.txt', 'w') as file:
            #create node to be used for all monitors
            r = ros_mon()

            curr_data = r.get_latest_arm_vert()
            val = 0.02
            change_data = create_json.change_vert(val)
            to_send = create_json.merge_json(curr_data, change_data)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()

            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    # if i == 0:
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break
            
            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(2, 0 , 0, 1)
            change_speed = create_json.change_speed(5.5)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break
            # time.sleep(5)

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(1, 0 , 0, 1)
            change_speed = create_json.change_speed(1)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break
            # time.sleep(5)

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(3, 0 , 0, -3.14)
            change_speed = create_json.change_speed(2)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break
            
            curr_data = r.get_latest_arm_vert()
            val = 0.1
            change_data = create_json.change_vert(val)
            to_send = create_json.merge_json(curr_data, change_data)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()

            # i = 0
            while True:
                # curr_angle = f"{float(json.loads(r.get_latest_arm_vert())['curr_vert_ang']):.1f}"
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    # if i == 0:
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            curr_data = r.get_latest_arm_vert()
            val = 0.01
            change_data = create_json.change_vert(val)
            to_send = create_json.merge_json(curr_data, change_data)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()

            # i = 0
            while True:
                # curr_angle = f"{float(json.loads(r.get_latest_arm_vert())['curr_vert_ang']):.1f}"
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    # if i == 0:
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(2, 0 , 0, 1)
            change_speed = create_json.change_speed(2)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break
            

            curr_data = r.get_latest_arm_vert()
            val = -0.35
            change_data = create_json.change_vert(val)
            to_send = create_json.merge_json(curr_data, change_data)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()

            # i = 0
            while True:
                # curr_angle = float(json.loads(r.get_latest_arm_vert())['curr_vert_ang'])
                # print('CURR VAL', curr_angle)
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    # if i == 0:
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    # i += 1
                    # if curr_angle == f"{val:.2f}":
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(2, 0 , 0.71, 0.71)
            change_speed = create_json.change_speed(2)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(2, 1 , 0.71, 0.71)
            change_speed = create_json.change_speed(2)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            curr_speed = r.get_latest_speed()
            curr_dist = r.get_latest_distance()
            change_nav = create_json.change_nav(2, 0 , 0, 0)
            change_speed = create_json.change_speed(2)
            to_send = create_json.merge_json(curr_speed, curr_dist)
            to_send = create_json.merge_json(to_send, change_speed)
            to_send = create_json.merge_json(to_send, change_nav)
            print("Sending command:\n ", to_send)
            create_json.send_data_to_larva(client_socket, to_send)
            start_time = time.time()
            print('sent')

            # i = 0
            while True:
                data = client_socket.recv(1024)
                if "valid move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('valid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    time.sleep(25)
                    break
                elif "wrong move on" in data.decode():
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print('invalid ', time_taken)
                    file.write(str(time_taken)+'\n')
                    break

            end_prog = create_json.create_gen_msg('end_program', -1)
            print(end_prog)
            create_json.send_data_to_larva(client_socket, end_prog)
            sys.exit(0)