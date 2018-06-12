from random import randint

from main.cell import Cell


class IO:

    @staticmethod
    def get_move(board, player):
        surrender, start_pos, end_pos = False, (0, 0), (0, 0)
        user_input = input(player.name + ", it's your turn now: ")  # user_input example: e3 -> f4
        if user_input == 'surrender':
            surrender = True
        else:
            data = user_input.replace(' ', '').split('->')  # data: ['e3', 'f4']
            start_pos = (board.BOARD_MARKUP.index(data[0][0]), int(data[0][1]) - 1)
            end_pos = (board.BOARD_MARKUP.index(data[1][0]), int(data[1][1]) - 1)
        return start_pos, end_pos, surrender

    @staticmethod
    def text_to_underlined(text):
        return "\033[4m" + text + "\033[0m"

    def draw_board(self, board, current_player):
        cells = board.cells
        first_line = "\n  |a|b|c|d|e|f|g|h|"
        grid = self.text_to_underlined(first_line) + "\n"

        y_range = range(board.BOARD_SIZE) if current_player.color is current_player.Color.BLACK \
            else reversed(range(board.BOARD_SIZE))
        for y in y_range:
            line = " " + str(y+1) + "|"
            for x in range(board.BOARD_SIZE):
                if cells[(x, y)].state == Cell.State.EMPTY:
                    line += " |"
                elif cells[(x, y)].state == Cell.State.BLACK:
                    line += "●|"
                elif cells[(x, y)].state == Cell.State.WHITE:
                    line += "○|"
                elif cells[(x, y)].state == Cell.State.WHITE_QUEEN:
                    line += "⚇|"
                elif cells[(x, y)].state == Cell.State.BLACK_QUEEN:
                    line += "⚉|"
            line = self.text_to_underlined(line) + "\n"
            grid += line
        print(grid)

    @staticmethod
    def create_players(colors):
        name1 = input("Player 1, enter your name: ")
        name2 = input("Player 2, enter your name: ")
        if randint(0, 2) == 0:
            color1 = colors[0]
            color2 = colors[1]
        else:
            color1 = colors[1]
            color2 = colors[0]
        return name1, color1, name2, color2
