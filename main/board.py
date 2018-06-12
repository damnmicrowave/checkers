from enum import Enum
from .cell import Cell


class Board:
    class MoveResult(Enum):
        SUCCSESSFUL_MOVE = 1
        SUCCSESSFUL_COMBAT = 2
        PROHIBITED = 0

    def __init__(self):
        self.BOARD_SIZE = 8
        self.BOARD_MARKUP = 'abcdefgh'
        self.cells = dict()

    def reset_board(self):

        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):

                state = Cell.State.EMPTY

                if y == 0 and x % 2 != 0:
                    state = Cell.State.WHITE
                elif y == 1 and x % 2 == 0:
                    state = Cell.State.WHITE
                elif y == 2 and x % 2 != 0:
                    state = Cell.State.WHITE
                elif y == 5 and x % 2 == 0:
                    state = Cell.State.BLACK
                elif y == 6 and x % 2 != 0:
                    state = Cell.State.BLACK
                elif y == 7 and x % 2 == 0:
                    state = Cell.State.BLACK

                position = (x, y)
                cell = Cell(state)

                self.cells[position] = cell

    def check_for_combat(self, current_player):
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if self.cells[(x, y)].state is Cell.State.BLACK \
                        and current_player.color is current_player.Color.BLACK:

                    try:
                        if self.cells[(x + 1, y + 1)].state is Cell.State.WHITE \
                                and self.cells[(x + 2, y + 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x + 1, y - 1)].state is Cell.State.WHITE \
                                and self.cells[(x + 2, y - 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x - 1, y + 1)].state is Cell.State.WHITE \
                                and self.cells[(x - 2, y + 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x - 1, y - 1)].state is Cell.State.WHITE \
                                and self.cells[(x - 2, y - 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass

                elif self.cells[(x, y)].state is Cell.State.WHITE \
                        and current_player.color is current_player.Color.WHITE:
                    try:
                        if self.cells[(x + 1, y + 1)].state is Cell.State.BLACK \
                                and self.cells[(x + 2, y + 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x + 1, y - 1)].state is Cell.State.BLACK \
                                and self.cells[(x + 2, y - 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x - 1, y + 1)].state is Cell.State.BLACK \
                                and self.cells[(x - 2, y + 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    try:
                        if self.cells[(x - 1, y - 1)].state is Cell.State.BLACK \
                                and self.cells[(x - 2, y - 2)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass

                if self.cells[(x, y)].state is Cell.State.BLACK_QUEEN \
                        and current_player.color is current_player.Color.BLACK:

                    counter = 1
                    try:
                        while self.cells[(x + counter, y + counter)].state is not Cell.State.WHITE_QUEEN \
                                and self.cells[(x + counter, y + counter)].state is not Cell.State.WHITE:
                            if self.cells[(x + counter, y + counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x + counter + 1, y + counter + 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1
                    try:
                        while self.cells[(x + counter, y - counter)].state is not Cell.State.WHITE_QUEEN \
                                and self.cells[(x + counter, y - counter)].state is not Cell.State.WHITE:
                            if self.cells[(x + counter, y - counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x + counter + 1, y - counter - 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1
                    try:
                        while self.cells[(x - counter, y + counter)].state is not Cell.State.WHITE_QUEEN \
                                and self.cells[(x - counter, y + counter)].state is not Cell.State.WHITE:
                            if self.cells[(x - counter, y + counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x - counter - 1, y + counter + 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1
                    try:
                        while self.cells[(x - counter, y - counter)].state is not Cell.State.WHITE_QUEEN \
                                and self.cells[(x - counter, y - counter)].state is not Cell.State.WHITE:
                            if self.cells[(x - counter, y - counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x - counter - 1, y - counter - 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass

                if self.cells[(x, y)].state is Cell.State.WHITE_QUEEN \
                        and current_player.color is current_player.Color.WHITE:

                    counter = 1
                    try:
                        while self.cells[(x + counter, y + counter)].state is not Cell.State.BLACK_QUEEN \
                                and self.cells[(x + counter, y + counter)].state is not Cell.State.BLACK:
                            if self.cells[(x + counter, y + counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x + counter + 1, y + counter + 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1

                    try:
                        while self.cells[(x + counter, y - counter)].state is not Cell.State.BLACK_QUEEN \
                                and self.cells[(x + counter, y - counter)].state is not Cell.State.BLACK:
                            if self.cells[(x + counter, y - counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x + counter + 1, y - counter - 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1
                    try:
                        while self.cells[(x - counter, y + counter)].state is not Cell.State.BLACK_QUEEN \
                                and self.cells[(x - counter, y + counter)].state is not Cell.State.BLACK:
                            if self.cells[(x - counter, y + counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x - counter - 1, y + counter + 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass
                    counter = 1
                    try:
                        while self.cells[(x - counter, y - counter)].state is not Cell.State.BLACK_QUEEN \
                                and self.cells[(x - counter, y - counter)].state is not Cell.State.BLACK:
                            if self.cells[(x - counter, y - counter)].state is Cell.State.EMPTY:
                                counter += 1
                            else:
                                raise KeyError
                        if self.cells[(x - counter - 1, y - counter - 1)].state is Cell.State.EMPTY:
                            return True
                    except KeyError:
                        pass

        return False

    def check_move(self, start_pos, end_pos, direction_reversed, current_player):
        dX = end_pos[0] - start_pos[0]
        dY = end_pos[1] - start_pos[1]
        combat, result, victim = self.check_for_combat(current_player), self.MoveResult.PROHIBITED, None
        if 0 <= start_pos[0] < self.BOARD_SIZE and \
                                0 <= start_pos[1] < self.BOARD_SIZE:

            targetCellState = self.cells[end_pos].state
            if targetCellState == Cell.State.EMPTY and \
                    ((self.cells[start_pos].state is Cell.State.BLACK or
                        self.cells[start_pos].state is Cell.State.BLACK_QUEEN and
                        current_player.color is current_player.Color.BLACK)
                        or
                        (self.cells[start_pos].state is Cell.State.WHITE or
                            self.cells[start_pos].state is Cell.State.WHITE_QUEEN and
                            current_player.color is current_player.Color.WHITE)):

                if abs(dX) == 2 and abs(dY) == 2 and combat:
                    victimCellPos = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
                    victimCellState = self.cells[victimCellPos].state
                    startCellState = self.cells[start_pos].state
                    result = self.MoveResult.SUCCSESSFUL_COMBAT if targetCellState != victimCellState \
                                                                   and startCellState != victimCellState else result

                elif (abs(dX) == 1 and dY == -1 and not direction_reversed) and not combat or \
                                (abs(dX) == 1 and dY == 1 and direction_reversed) and not combat:
                    result = self.MoveResult.SUCCSESSFUL_MOVE

                if self.cells[start_pos].state is Cell.State.WHITE_QUEEN \
                        or self.cells[start_pos].state is Cell.State.BLACK_QUEEN:
                    is_empty = True
                    if direction_reversed:

                        if dX > 0 and dY > 0:
                            reverser_x, reverser_y = 1, 1
                        elif dX < 0 and dY > 0:
                            reverser_x, reverser_y = -1, 1
                        elif dX > 0 and dY < 0:
                            reverser_x, reverser_y = 1, -1
                        else:
                            reverser_x, reverser_y = -1, -1
                            for i in range(1, abs(dX)):
                                if self.cells[start_pos[0] + reverser_x * i, start_pos[1] - reverser_y * i].state \
                                        is not Cell.State.EMPTY:
                                    is_empty = False
                    else:

                        if dX > 0 and dY > 0:
                            reverser_x, reverser_y = 1, 1
                        elif dX < 0 and dY > 0:
                            reverser_x, reverser_y = -1, 1
                        elif dX > 0 and dY < 0:
                            reverser_x, reverser_y = 1, -1
                        else:
                            reverser_x, reverser_y = -1, -1
                            for i in range(1, abs(dX)):
                                if self.cells[start_pos[0] + reverser_x * i, start_pos[1] + reverser_y * i].state \
                                        is not Cell.State.EMPTY:
                                    is_empty = False
                    if is_empty and not combat:
                        result = self.MoveResult.SUCCSESSFUL_MOVE
                for x in range(int(dX / abs(dY)), dX, int(dX / abs(dY))):
                    for y in range(int(abs(dX) / dY), dY, int(abs(dX) / dY)):
                        if self.cells[start_pos].state is Cell.State.BLACK_QUEEN \
                                and self.cells[(start_pos[0] + x, start_pos[1] + y)].state is Cell.State.WHITE_QUEEN \
                                or self.cells[(start_pos[0] + x, start_pos[1] + y)].state is Cell.State.WHITE:
                            result, victim = self.MoveResult.SUCCSESSFUL_COMBAT, \
                                             self.cells[(start_pos[0] + x, start_pos[1] + y)]
                        elif self.cells[start_pos].state is Cell.State.WHITE_QUEEN \
                                and self.cells[(start_pos[0] + x, start_pos[1] + y)].state is Cell.State.BLACK_QUEEN \
                                or self.cells[(start_pos[0] + x, start_pos[1] + y)].state is Cell.State.BLACK:
                            result, victim = self.MoveResult.SUCCSESSFUL_COMBAT, \
                                             self.cells[(start_pos[0] + x, start_pos[1] + y)]

        return result, victim

    def make_move(self, start_pos, end_pos, direction_reversed, current_player):
        moveResult, victim = self.check_move(start_pos, end_pos, direction_reversed, current_player)
        if moveResult is self.MoveResult.SUCCSESSFUL_MOVE:
            self.cells[end_pos].state = self.cells[start_pos].state
            self.cells[start_pos].state = Cell.State.EMPTY
        elif moveResult is self.MoveResult.SUCCSESSFUL_COMBAT and victim is not None:
            self.cells[end_pos].state = self.cells[start_pos].state
            self.cells[start_pos].state = Cell.State.EMPTY
            victim.state = Cell.State.EMPTY
        elif moveResult is self.MoveResult.SUCCSESSFUL_COMBAT:
            self.cells[end_pos].state = self.cells[start_pos].state
            self.cells[start_pos].state = Cell.State.EMPTY
            victimCellPos = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
            self.cells[victimCellPos].state = Cell.State.EMPTY
        if moveResult is not self.MoveResult.PROHIBITED \
                and (end_pos[1] == 0 and self.cells[end_pos].state is Cell.State.BLACK):
            self.cells[end_pos].state = Cell.State.BLACK_QUEEN
        elif end_pos[1] == 7 and self.cells[end_pos].state is Cell.State.WHITE:
            self.cells[end_pos].state = Cell.State.WHITE_QUEEN

        return moveResult
