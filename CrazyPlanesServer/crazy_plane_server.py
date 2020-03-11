import asyncio
import time
import json

from CrazyPlaneCommon.colored_plane import ColoredPlane
from CrazyPlanesCore import GameBoard, StandardStrategy
from CrazyPlanesServer.web_socket_server import WebSocketServer


class CrazyPlaneServer:
    def __init__(self):
        self.server = WebSocketServer("localhost", 5000, self.run)

    async def run(self):
        size_response = await self.server.receive()
        print(size_response)
        size_dto = json.loads(size_response)
        width, height = size_dto['width'], size_dto['height']

        planes_response = await self.server.receive()
        planes_dto = json.loads(planes_response)
        planes = []

        for plane in planes_dto:
            planes.append(ColoredPlane(plane["color"], StandardStrategy(width, height)))

        game_board = GameBoard(width, height, planes)

        if await self.server.receive() == "start":
            await self.start_game(game_board)

    async def start_game(self, game_board):
        done = False
        while not done:
            state = game_board.run()
            done = game_board.check_if_done()
            for plane in state:
                await self.server.send(plane.display())
                time.sleep(0.1)

    def start_server(self):
        asyncio.get_event_loop().run_until_complete(self.server.start_server)
        asyncio.get_event_loop().run_forever()


def main():
    server = CrazyPlaneServer()
    server.start_server()


if __name__ == '__main__':
    main()
