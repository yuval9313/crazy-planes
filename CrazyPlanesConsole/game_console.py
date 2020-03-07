import time
import json
from CrazyPlanesCore import GameBoard, StandardStrategy
from CrazyPlaneCommon.colored_plane import ColoredPlane


def run(game_board):
    done = False
    while not done:
        state = game_board.run()
        done = game_board.check_if_done()
        for plane in state:
            display = json.loads(plane.display())
            print(f"plane: {display['color']} is in {display['pos']} score: {display['score']}")
            time.sleep(0.1)


def main():
    print("Welcome to crazy planes")
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    game_board = GameBoard(width, height, [
        ColoredPlane("red", StandardStrategy(width, height)),
        ColoredPlane("yellow", StandardStrategy(width, height)),
        ColoredPlane("blue", StandardStrategy(width, height))
    ])

    run(game_board)


if __name__ == '__main__':
    main()
