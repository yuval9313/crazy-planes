import websockets
import struct


class WebSocketServer:
    def __init__(self, address, port, run_callback):
        self.start_server = websockets.serve(self.run, address, port)
        self.web_socket = None
        self.run_callback = run_callback

    def run(self, web_socket, path):
        self.web_socket = web_socket
        self.run_callback()

    async def receive(self):
        return await self.web_socket.recv()

    async def send(self, message):
        message_len = struct.pack('!I', len(message))
        await self.web_socket.send(message_len)
        await self.web_socket.send(message)
