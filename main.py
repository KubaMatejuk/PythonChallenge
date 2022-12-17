import pygame
from gameboard import GameBoard

from control import select_column_by_key, select_column_by_mouse

pygame.init()
window = pygame.display.set_mode((1280, 720))


def main():
    run = True
    game_board = GameBoard(window)
    current_color = 'yellow'

    # background = pygame.image.load("background.png")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when usr will close window
                run = False

        keys = pygame.key.get_pressed()
        # probably need to add similar as above for mouse

        column = select_column_by_key(keys)
        if column:
            game_board.drop_token(column, current_color)
            if game_board.check_success():
                # provide info about winner
                run = False
            if current_color == 'red':
                current_color = 'yellow'
            else:
                current_color = 'red'

        window.fill((0, 0, 0))
        # window.blit(background, (0, 0))  # rysowanie tła
        game_board.draw()
        for token in game_board.tokens:
            token.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    main()
