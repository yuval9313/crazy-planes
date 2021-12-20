from CrazyPlanesCore import StandardStrategy, GameStrategy


class StandardFactory:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_strategy(self) -> GameStrategy:
        return StandardStrategy(self.width, self.height)
