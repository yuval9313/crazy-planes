import websockets
import asyncio
import struct

async def hello(websocket, path):
    print('Server started')
    
    while True:
        name = await websocket.recv()
        print(f'< {name}')

        greeting = f'Hello {name}!'
        message_len = struct.pack('!I', len(greeting))
        print(message_len)
        await websocket.send(message_len)
        await websocket.send(greeting)
        print(f'> {greeting}')

start_server = websockets.serve(hello, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
