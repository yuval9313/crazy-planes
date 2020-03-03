from abc import ABCMeta, abstractmethod


class GameStrategy(metaclass=ABCMeta):
    @abstractmethod
    def play(self, pos, board_state):
        raise NotImplementedError("This is an abstract method which needs to be implemented")
