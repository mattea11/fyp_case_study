# import websocket

# def on_message(ws, message):
#     print("WebSocket message received: " + message)

# def on_error(ws, error):
#     print("WebSocket error: " + str(error))

# def on_close(ws):
#     print("WebSocket closed")

# def on_open(ws):
#     print("WebSocket opened")

# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://localhost:8080/Larva_socket",
#                                 on_message = on_message,
#                                 on_error = on_error,
#                                 on_close = on_close,
#                                 on_open = on_open)
#     ws.run_forever()


# import websocket

# # websocket.enableTrace(True)
# ws = websocket.WebSocket()
# ws.connect("ws://172.30.176.1:8080/Larva_socket")
# print('connected')
# ws.send("Hello, Server")
# print('sent msg')
# print('woot woot recv' + ws.recv())
# ws.close()

import websocket

# Specify the WebSocket server URL
websocket_url = "ws://172.30.176.1:8080"

# Connect to the WebSocket server
ws = websocket.create_connection(websocket_url)

# Send a message to the server
ws.send("Hello from Python!")

# Receive messages from the server
while True:
    message = ws.recv()
    print("Received message: ", message)

# Close the WebSocket connection
ws.close()