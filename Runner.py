from larva_client import larva_client
from ros_mon import ros_mon_listener

import socket
import json

if __name__ == '__main__':

    # start_client()
    HOST = "192.168.4.21"
    PORT = 8080

    # Create a TCP socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Receive a response from the server
    data = client_socket.recv(1024)
    print('Received from server: ', data.decode())

    # message = '{"mast_angle_horiz": 0}'

    # larva_client.send_data_to_larva(client_socket, message)

    # # ros_mon_listener()

    # message = '{"mast_angle_vert": 1}'

    # larva_client.send_data_to_larva(client_socket, message)

    # collect data using ros_mon_listener
    collected_data = {}
    ros_mon_listener(collected_data)

    # send collected data to server
    merged_json = larva_client.merge_json(json.dumps(collected_data))
    larva_client.send_data_to_larva(client_socket, merged_json)
