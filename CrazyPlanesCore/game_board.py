import random


class GameBoard:
    def __init__(self, width, height, planes):
        self.width = width
        self.height = height
        self.board_state = planes
        self.bootstrap()

    def bootstrap(self):
        positions = self.get_positions()
        while not self.verify_positions(positions):
            positions = self.get_positions()

        for i in range(len(self.board_state)):
            plane = self.board_state[i]
            plane.pos = positions[i]

    def get_positions(self):
        return [
            (random.randrange(0, self.width),
             random.randrange(0, self.height))
            for i in range(len(self.board_state))
        ]

    @staticmethod
    def verify_positions(positions) -> bool:
        for pos in positions:
            if positions.count(pos) == 1:
                return True

        return False

    def run(self) -> list:
        for plane in self.board_state:
            plane.move(self.board_state)

        return self.board_state

    def check_if_done(self) -> bool:
        for plane in self.board_state:
            if self.board_state.count(plane) > 1:
                return True

            if plane.score == 1000:
                return True

        return False
