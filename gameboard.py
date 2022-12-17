import pygame
import numpy
from disc import Disc

#MMI

class GameBoard:
    def __init__(self, window):
        self.window = window
        self.tokens = []
        self.width = 1652
        # self.height = self.image.get_height()

        # placeholder for array with current state
        # self.game_board_state = numpy.array()
        pass

    def draw(self):
        pass

    def drop_token(self, column_no, color):
        #JM
        x_for_column_list = []
        x = 0
        y = 0
        # above to be updated basing on column number and game board size

        token = Disc(color, x, y)
        self.tokens.append(token)
        # add 'animation'
        # update board state
        pass

    def check_success(self) -> bool:
        # DP
        pass
