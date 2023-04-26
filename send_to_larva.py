import websocket
import time

# Specify the WebSocket server URL
websocket_url = "ws://192.168.4.21:8080"
print('this is the ip ' + websocket_url)

try:
    print('trying to connect')
    # Connect to the WebSocket server
    ws = websocket.create_connection(websocket_url)


except Exception as e:
    print("Error:", e)
