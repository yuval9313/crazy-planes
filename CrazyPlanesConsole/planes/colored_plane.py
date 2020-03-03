from CrazyPlanesCore import Plane


class ColoredPlane(Plane):
    def __init__(self, color, game_strategy):
        super().__init__(game_strategy)
        self._color = color

    def display(self):
        return f"{self._color} is in {self.pos} Score: {self._game_strategy.score}"
