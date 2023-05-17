import json

class create_json:
    #functions related to creating commands to be verified and sending them
    def change_nav( x, y, z, w):
        data = {
            "new_nav": {
                "x": x,
                "y": y,
                "turn_z": z,
                "turn_w": w
            }
            # ,
            # "change_speed": speed
        }
        return json.dumps(data)

    def change_speed(speed):
        my_dict = {'change_speed': speed}
        json_object = json.dumps(my_dict)
        return json_object

    def change_vert(angle):
        my_dict = {'change_vert_ang': angle}
        json_object = json.dumps(my_dict)
        return json_object
        
    # def curr_dist(distances):
    #     my_dict = {'curr_distances': distances}
    #     json_object = json.dumps(my_dict)
    #     return json_object

    # def curr_speed(speed):
    #     my_dict = {'curr_speed': speed}
    #     json_object = json.dumps(my_dict)
    #     return json_object

    # def curr_mast_ang(angle):
    #     my_dict = {'curr_vert_ang': angle}
    #     json_object = json.dumps(my_dict)
    #     return json_object
    
    def merge_json(json1, json2):
        # Convert the JSON strings to Python dictionaries
        dict1 = json.loads(json1)
        dict2 = json.loads(json2)
        # Merge the dictionaries
        merged_dict = {**dict1, **dict2}
        # Convert the merged dictionary back to a JSON string
        merged_json = json.dumps(merged_dict) + '\n'
        return merged_json
    
    def create_gen_msg(attribute, msg):
        my_dict = {attribute: msg}
        json_object = json.dumps(my_dict)
        return json_object

    # Callback function for sending JSON objects to the server
    def send_data_to_larva(client_socket, json_obj):
        client_socket.sendall(json_obj.encode())
