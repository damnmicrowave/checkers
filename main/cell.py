from enum import Enum


class Cell:

    class State(Enum):
        WHITE = 1
        BLACK = 2
        WHITE_QUEEN = 3
        BLACK_QUEEN = 4
        EMPTY = 0

    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
