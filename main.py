import pygame
import time
from gameboard import GameBoard

from control import select_column_by_key, select_column_by_mouse
from display import text_object, button
from tkinter import *
from tkinter import messagebox


pygame.init()
pygame.mixer.init()
# window = pygame.display.set_mode((1652, 1416)) #zmniejszyc razy 2
window = pygame.display.set_mode((770, 760))
pygame.display.set_caption("Four in the Row")


def main():
    # JM - ekran powitalny
    # DP - menu

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
        text_object(window, (current_color + " player turn"), font, text_color, 280, 10)

        column = select_column_by_key(keys)
        if column:
            try:
                game_board.drop_token(column, current_color)

                if game_board.check_success(current_color):
                    # provide info about winner
                    Tk().wm_withdraw()  # to hide the main window
                    messagebox.showinfo("Success", f"{current_color.upper()} player won!")
                    print(f"{current_color} won!")
                    run = False
                if game_board.check_draw():
                    Tk().wm_withdraw()
                    messagebox.showinfo("Draw", "It's a draw!")
                    run = False
                if current_color == 'red':
                    current_color = 'yellow'
                else:
                    current_color = 'red'
                time.sleep(0.25)
            except Exception as e:
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showwarning("Warning", e)

        game_board.draw()
        for token in game_board.tokens:
            token.draw(window)

        pygame.display.update()


def menu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((0, 0, 0))
        text_object(window, "CONNECT", pygame.font.SysFont("arial", 40), (255, 255, 255), 250, 20)
        text_object(window, "4", pygame.font.SysFont("arial", 60), (255, 0, 0), 450, 10)

        button(window, "Start a game", 250, 350, 230, 50, None, None, main)

        # TODO: singleplayer choice, multiplayer choice, exit, settings
        # TODO: find a better way to manage fonts and colors of text objects

        pygame.display.update()


if __name__ == "__main__":
    menu()
