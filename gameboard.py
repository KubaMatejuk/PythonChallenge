import pygame
import numpy as np
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
        self.width = 770
        # self.height = self.image.get_height()
        self.height = 660
        self.number_of_columns = 7
        self.number_of_rows = 6
        self.game_board_state = np.zeros((self.number_of_rows, self.number_of_columns)).astype(int)

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
        x_for_column_list = [0, 0, 110, 220, 330, 440, 550, 660, 770]
        x = x_for_column_list[column_no]
        y = 100
        # above to be updated basing on column number and game board size

        # updating board state
        i = self.number_of_rows - 1
        while self.game_board_state[(i, column_no - 1)] and i >= 0:
            i -= 1
        if i < 0:
            incorrect_sound = pygame.mixer.Sound('sound/incorrect_move.mp3')
            pygame.mixer.Sound.play(incorrect_sound)
            raise Exception(f'Column {column_no} is full - cannot add more discs to that column.')
        else:
            drop_sound = pygame.mixer.Sound('sound/drop_sound.mp3')
            pygame.mixer.Sound.play(drop_sound)
            self.game_board_state[(i, column_no - 1)] = get_color_id(color)
        token = Disc(color, x, y)
        self.tokens.append(token)

        # add 'animation'
        for j in range(6):
            if j < i:
                self.tokens[-1].y += 110
                self.draw()
                for token in self.tokens:
                    token.draw(self.window)
                pygame.display.update()

    def check_success(self, color: str) -> bool:
        """
        Checks if 4 of the same colored discs in a row are connected (either vertically, horizontally, or diagonally)

        param: color_id - a color of players discs
        """
        # horizontal check
        color_id = get_color_id(color)  # get index of color

        for row in range(self.number_of_rows):
            if str(color_id) * 4 in ''.join(map(str, list(self.game_board_state[row]))):
                return True

        # vertical check
        for column in range(self.number_of_columns):
            if str(color_id) * 4 in ''.join(map(str, list(self.game_board_state[:, column]))):
                return True

        # diagonal check
        for row in range(self.number_of_rows - 3):  # use 3 to create minor matrices 4x4 and calculate trace of matrices
            for column in range(self.number_of_columns - 3):
                sub_game_board_state = self.game_board_state[row:row + 4, column:column + 4]

                # diagonal is the list of elements a_{ij} in matrix where i == j, condition for diagonal check
                # searches for 4 the same values in the main diagonal of a matrix,
                # to check positive slopes it is required to use mirror reflection using fliplr
                if all(np.diagonal(sub_game_board_state) == color_id) or \
                   all(np.diagonal(np.fliplr(sub_game_board_state)) == color_id):
                    return True

    def check_draw(self):
        # check for a draw
        if all(self.game_board_state.flatten() != 0):
            return True
