import pygame
import time
from gameboard import GameBoard

from control import select_column_by_key, select_column_by_mouse
import player


# AB
pygame.init()
pygame.mixer.init()
# window = pygame.display.set_mode((1652, 1416)) #zmniejszyc razy 2
window = pygame.display.set_mode((770, 760))
pygame.display.set_caption("Four in the Row")


def main():
    run = True
    game_board = GameBoard(window)
    current_color = 'yellow'

    # background = pygame.image.load("background.png")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when usr will close window
                run = False
        window.fill((0, 0, 0))
        background = pygame.image.load("4intherow_background.png")
        window.blit(background, (0, 0))  # rysowanie tła
        keys = pygame.key.get_pressed()
        # probably need to add similar as above for mouse

        # display which player's turn is it
        font = pygame.font.SysFont("arial", 40)
        if current_color == 'yellow':
            text_color = (255, 255, 50)  # yellow color
        else:
            text_color = (255, 0, 0)  # red color
        player.draw(window, (current_color + " player turn"), font, text_color, 280, 10)

        column = select_column_by_key(keys)
        if column:
            game_board.drop_token(column, current_color)
            if game_board.check_success(current_color):
                # provide info about winner
                print(f"{current_color} won!")
                run = False
            if current_color == 'red':
                current_color = 'yellow'
            else:
                current_color = 'red'
            time.sleep(0.25)



        game_board.draw()
        for token in game_board.tokens:
            token.draw(window)


        pygame.display.update()


if __name__ == "__main__":
    main()
