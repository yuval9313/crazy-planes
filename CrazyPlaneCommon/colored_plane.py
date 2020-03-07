import json
from CrazyPlanesCore import Plane


class ColoredPlane(Plane):
    def __init__(self, color, game_strategy):
        super().__init__(game_strategy)
        self._color = color

    def display(self):
        return json.dumps({"color": self._color, "pos": self.pos, "score": self._game_strategy.score})
