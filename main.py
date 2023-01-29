import pygame
import time
from gameboard import GameBoard

from control import select_column_by_key, select_column_by_mouse
from display import text_object, button
from tkinter import *
from tkinter import messagebox


BLACK_COLOR = (0, 0, 0)
BUTTON_IDLE_COLOR = (0, 82, 204)
BUTTON_ACTIVE_COLOR = (77, 148, 255)
BUTTON_TEXT_IDLE_COLOR = (0, 0, 0)
BUTTON_TEXT_ACTIVE_COLOR = (255, 255, 255)
MENU_TEXT_COLOR = (0, 0, 0)
MENU_TITLE_COLOR = (51, 133, 255)
MENU_DISC_COLOR = (204, 224, 255)

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

        window.fill(BLACK_COLOR)  # clear all drawings
        background = pygame.image.load("4intherow_background.png")
        background.set_alpha(125)  # display a transparent image to distinguish menu and gameplay
        window.blit(background, (0, 0))  # use 4intherow board as a background

        # visualization in the menu: a disc following the mouse's position only if mouse's coordinates are inside window
        mouse = pygame.mouse.get_pos()
        if 0 < mouse[0] < 769 and 759 > mouse[1] > 110:
            x_circle = int(mouse[0]/110)*110 + 55
            y_circle = int(mouse[1]/110 - 1)*110+100 + 55

            pygame.draw.circle(window, MENU_DISC_COLOR, (x_circle, y_circle), 55)

        # text objects and buttons
        text_object(window, "CONNECT 4", pygame.font.SysFont("arial", 120), MENU_TITLE_COLOR, 40, 30)

        # TODO: how we can deal with different length of text in button? Find a way to center text automatically
        button(window, " Singleplayer", 200, 200, 375, 75, BUTTON_IDLE_COLOR, BUTTON_ACTIVE_COLOR,
               BUTTON_TEXT_IDLE_COLOR, BUTTON_TEXT_ACTIVE_COLOR, main)

        button(window, "  Multiplayer", 200, 300, 375, 75, BUTTON_IDLE_COLOR, BUTTON_ACTIVE_COLOR,
               BUTTON_TEXT_IDLE_COLOR, BUTTON_TEXT_ACTIVE_COLOR, main)

        button(window, "     Settings", 200, 400, 375, 75, BUTTON_IDLE_COLOR, BUTTON_ACTIVE_COLOR,
               BUTTON_TEXT_IDLE_COLOR, BUTTON_TEXT_ACTIVE_COLOR, main)

        button(window, "        Exit", 200, 500, 375, 75, BUTTON_IDLE_COLOR, BUTTON_ACTIVE_COLOR,
               BUTTON_TEXT_IDLE_COLOR, BUTTON_TEXT_ACTIVE_COLOR, quit_game)

        # TODO: find a better way to manage fonts of text objects

        pygame.display.flip()


def quit_game():
    pygame.display.quit()
    exit()

    
if __name__ == "__main__":
    menu()
