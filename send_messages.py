import asyncio
import websockets

async def send_file_contents(websocket, path):
    with open(path, 'r') as f:
        contents = f.read()
        await websocket.send(contents)

async def serve(websocket, path):
    await send_file_contents(websocket, 'lol.txt')

async def main():
    async with websockets.serve(serve, 'localhost', 8080):
        await asyncio.Future()  # keep the server running

if __name__ == '__main__':
    asyncio.run(main())
