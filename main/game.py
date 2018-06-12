import os

from .player import Player
from .board import Board
from .i_o import IO

io = IO()


class Game:
    board = Board()
    player1 = None
    player2 = None
    last_player = None
    current_player = None
    surrender = False
    first_round = True

    def game_start(self):
        colors = (Player.Color.WHITE, Player.Color.BLACK)
        name1, color1, name2, color2 = io.create_players(colors)
        self.player1, self.player2 = Player(name1, color1), Player(name2, color2)
        self.current_player = self.player1 if self.player1.color is Player.Color.WHITE else self.player2
        self.board.reset_board()
        self.mainloop()

    def get_direction(self):

        direction_reversed = True

        if self.current_player.color is Player.Color.BLACK:
            direction_reversed = False

        return direction_reversed

    def game_stop(self, winner):
        io.draw_board(self.board, self.current_player)
        print(winner.name + " wins!")
        exit()

    def get_winner(self):
        if self.surrender:
            winner = self.player2 if self.last_player == self.player1 else self.player1
        elif self.player1.score == 12:
            winner = self.player1
        elif self.player2.score == 12:
            winner = self.player2
        else:
            winner = None

        return winner

    def io_stuff(self):
        os.system('clear')

        if self.first_round:
            colors = ('○', '●') if self.player1.color is Player.Color.WHITE else ('●', '○')
            print(self.player1.name + ", your color is " + colors[0])
            print(self.player2.name + ", your color is " + colors[1])
            print('\nTo make move, write e. g. "b3->c4"\nTo surrender, type "surrender"')
            self.first_round = False
        else:
            print(self.player1.name + ": " + str(self.player1.score))
            print(self.player2.name + ": " + str(self.player2.score))

        io.draw_board(self.board, self.current_player)
        start_pos, end_pos, self.surrender = io.get_move(self.board, self.current_player)
        if self.surrender:
            self.game_stop(self.get_winner())
        return start_pos, end_pos

    def switch_player(self):
        self.last_player = self.player1 if self.last_player is self.player2 else self.player2
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2

    def update_score(self):
        if self.last_player is self.player2:
            self.player1.score += 1
        else:
            self.player2.score += 1

    def mainloop(self):
        winner = None
        while winner is None:
            result = Board.MoveResult.PROHIBITED
            while result is Board.MoveResult.PROHIBITED:
                start_pos, end_pos = self.io_stuff()
                direction = self.get_direction()
                result = self.board.make_move(start_pos, end_pos, direction, self.current_player)

            if result is Board.MoveResult.SUCCSESSFUL_MOVE:
                self.switch_player()
            elif result is Board.MoveResult.SUCCSESSFUL_COMBAT and self.board.check_for_combat(self.current_player):
                self.update_score()
            else:
                self.update_score()
                self.switch_player()
            winner = self.get_winner()

        self.game_stop(winner)
