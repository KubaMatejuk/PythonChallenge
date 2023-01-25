import pygame


def text_object(window, text, font, text_colour, x, y):
    text_image = font.render(text, True, text_colour)
    window.blit(text_image, (x, y))


def button(window, text, x, y, button_width, button_height, button_idle_color, button_action_color, text_idle_color,
           text_action_color, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(window, button_idle_color, (x, y, button_width, button_height))
    text_object(window, text, pygame.font.SysFont("arial", int(button_height*0.8)), text_idle_color, x, y)

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:
        pygame.draw.rect(window, button_action_color, (x, y, button_width, button_height))
        text_object(window, text, pygame.font.SysFont("arial", int(button_height*0.8)), text_action_color, x, y)
        if click[0] == 1:
            action()
