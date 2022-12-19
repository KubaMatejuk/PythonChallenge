import pygame
import numpy
from disc import Disc


# MMI

def get_color_id(color):
    if color == 'red':
        color_id = 1
    else:
        color_id = 2
    return color_id


class GameBoard:
    def __init__(self, window):
        self.window = window
        self.tokens = []
        # self.width = 1652
        # self.height = self.image.get_height()
        self.number_of_columns = 7
        self.number_of_rows = 6
        self.game_board_state = numpy.zeros((self.number_of_rows, self.number_of_columns))

        pass

    def draw(self):
        pass

    def drop_token(self, column_no, color):
        """

        :param column_no: number of column to which we drop disc - number between 1 and 7 inclusively
        :param color:
        :return:
        """
        # JM
        x_for_column_list = [0, 160, 320, 480, 640, 800, 960, 1120]
        x = x_for_column_list[column_no]
        y = 0
        # above to be updated basing on column number and game board size

        # updating board state
        i = self.number_of_rows - 1
        while self.game_board_state[(i, column_no - 1)]:
            i -= 1
        if i == 0:
            raise Exception(f'Column {column_no} is full - cannot add more discs to that column.')
        else:
            self.game_board_state[(i, column_no - 1)] = get_color_id(color)
        token = Disc(color, x, y)
        self.tokens.append(token)

        # add 'animation'
        for j in range(6):
            if j < i:
                self.tokens[-1].y += 100
                self.draw()
                for token in self.tokens:
                    token.draw(self.window)
                pygame.display.update()

    def check_success(self) -> bool:
        # DP
        pass
