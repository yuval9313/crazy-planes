from abc import ABC, abstractmethod


class Plane(ABC):
    def __init__(self, game_strategy):
        super().__init__()
        self.pos = ()
        self._game_strategy = game_strategy

    def move(self, board_state):
        self.pos = self._game_strategy.play(self.pos, board_state)
        return self.pos

    @property
    def score(self):
        return self._game_strategy.score

    @abstractmethod
    def display(self):
        raise NotImplementedError("This is an abstract method which needs to be overridden")
