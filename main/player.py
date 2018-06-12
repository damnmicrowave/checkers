from enum import Enum
from .i_o import IO

io = IO()


class Player:

    class Color(Enum):
        WHITE = 1
        BLACK = 2
        NONE = 0

    def __init__(self, name, color):
        self._name, self._color = name, color
        self._score = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
