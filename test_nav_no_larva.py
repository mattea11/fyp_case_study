# import websocket
# import json
# import math

# def send_nav_command(x, y, z, turn_angle):
#     msg = {}
#     header = {}
#     pose = {}
#     position = {}
#     orientation = {}

#     angle_in_radians = turn_angle * (math.pi / 180.0) 
#     sin_half_angle = math.sin(angle_in_radians / 2)
#     cos_half_angle = math.cos(angle_in_radians / 2)

#     header["frame_id"] = "odom"
    
#     position["x"] = x
#     position["y"] = y
#     position["z"] = z
    
#     orientation["x"] = 0
#     orientation["y"] = 0
#     orientation["z"] = sin_half_angle
#     orientation["w"] = cos_half_angle
    
#     pose["position"] = position
#     pose["orientation"] = orientation

#     msg["op"] = "publish"
#     msg["topic"] = "/move_base_simple/goal"
#     msg["msg"] = {"header": header, "pose": pose}
    
#     return json.dumps(msg)

# def send_speed_command(speed):
#     data = {}
#     data["x"] = speed
#     data["y"] = 0.0
#     data["z"] = 0.0

#     angular_velocity = {}
#     angular_velocity["x"] = 0.0
#     angular_velocity["y"] = 0.0
#     angular_velocity["z"] = 0.0

#     twist = {}
#     twist["linear"] = data
#     twist["angular"] = angular_velocity

#     msg = {}
#     msg["op"] = "publish"
#     msg["topic"] = "/curiosity_mars_rover/ackermann_drive_controller/cmd_vel"
#     msg["msg"] = twist
#     msg["type"] = "geometry_msgs/Twist"
    
#     return json.dumps(msg)

# def send_mast_vert_command(angle):
#     data = {}
#     data["data"] = angle 

#     msg = {}
#     msg["op"] = "publish"
#     msg["topic"] = "/curiosity_mars_rover/mast_cameras_joint_position_controller/command"
#     msg["msg"] = data
#     msg["type"] = "std_msgs/Float64"

#     return json.dumps(msg)

# if __name__ == '__main__':  
#     rosbridge_address = "ws://localhost:9090"

#     # Connect to the ROSbridge server
#     websocket_connection = websocket.create_connection(rosbridge_address)



#     # Send the JSON message to the ROSbridge server
#     websocket_connection.send(json.dumps(json_message))

#     # Close the websocket connection
#     websocket_connection.close()

import json
import websocket
import time

def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket opened")
    send_messages(ws)

# /curiosity_mars_rover/ackermann_drive_controller/cmd_vel
def send_messages(ws):
    print('HELLOO')
    messages = [
        # {"op": "publish", "topic": "/curiosity_mars_rover/mast_cameras_joint_position_controller/command", "msg": {"data":-1.0}},
        # {"op": "publish", "topic": "/curiosity_mars_rover/mast_cameras_joint_position_controller/command", "msg": {"data":1.0}},
        # {"op": "publish", "topic": "/curiosity_mars_rover/mast_cameras_joint_position_controller/command", "msg": {"data":0.0}},
        {"op": "publish", "topic": '/move_base_simple/goal', "msg": { "header": { "frame_id": "odom" }, "pose": { "position": { "x": 4.0, "y": 0.0, "z": 0.0 }, "orientation": { "x": 0.0, "y": 0.0, "z": 0.0, "w":1.0}}}},
        # {"op": "publish", "topic": '/move_base_simple/goal', "msg": { "header": { "frame_id": "odom" }, "pose": { "position": { "x": 2.0, "y": 0.0, "z": 0.0 }, "orientation": { "x": 0.0, "y": 0.0, "z": 0.7071067811865476, "w": 0.7071067811865475 }}}},
        # {"op": "publish", "topic": '/move_base_simple/goal', "msg": { "header": { "frame_id": "odom" }, "pose": { "position": { "x": 3.0, "y": 1.0, "z": 0.0 }, "orientation": { "x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0 }}}},
    ]
    i = 0
    for msg in messages: #sedning teh commands
        # if(i == 0):
            ws.send(json.dumps(msg))
            time.sleep(4)
        # else:
        #     if("/curiosity_mars_rover/mast_cameras_joint_position_controller/command" in msg["topic"]):
        #         #subscribe to topic '/curiosity_mars_rover/mast_cameras_joint_position_controller/state' and spin till process_value == the data value then break to send the next message
        #     elif("/move_base_simple/goal" in msg["topic"]):
        #         #subscribe to topic '/move_base/result' and spin till the callbac function return true then break to send the next message

        # i+=1

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090/")
    ws.on_message = on_message
    ws.on_error = on_error
    ws.on_close = on_close
    ws.on_open = on_open
    acknowledged_messages = set()
    ws.run_forever()
