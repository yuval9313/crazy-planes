import random
from CrazyPlanesCore import GameStrategy


class StandardStrategy(GameStrategy):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.score = 0

    def play(self, pos, game_state):
        neighbors = self.neighbors(1, pos)
        random.shuffle(neighbors)

        available_positions = neighbors[:]
        for plane in game_state:
            if available_positions.count(plane.pos) > 0:
                available_positions.remove(plane.pos)

        if len(available_positions) == len(neighbors):
            self.score += 1
        return available_positions[0]

    def neighbors(self, radius, pos) -> list:
        row_number, column_number = pos
        column_range = range(column_number - radius, column_number + 1 + radius)
        row_range = range(row_number - radius, row_number + 1 + radius)
        positions = [
            (i, j)
            for i in row_range
            for j in column_range
            if 0 <= i < self.width - 1 and 0 <= j < self.height - 1 and (i, j) != pos
        ]

        return positions
