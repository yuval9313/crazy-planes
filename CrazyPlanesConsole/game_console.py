import time

from CrazyPlanesCore import GameBoard, StandardStrategy
from CrazyPlanesConsole.planes.colored_plane import ColoredPlane


class GameConsole:
    def __init__(self, planes):
        self.game_board = GameBoard(width, height, planes)
        self._done = False

    def run(self):
        while not self._done:
            state = self.game_board.run()
            self._done = self.game_board.check_if_done()
            for plane in state:
                print(plane.display())
                time.sleep(0.1)


if __name__ == '__main__':
    print("Welcome to crazy planes")
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    game = GameConsole([
        ColoredPlane("red", StandardStrategy(width, height)),
        ColoredPlane("yellow", StandardStrategy(width, height)),
        ColoredPlane("blue", StandardStrategy(width, height))
    ])

    game.run()
