import pygame


def text_object(window, text, font, text_colour, x, y):
    text_image = font.render(text, True, text_colour)
    window.blit(text_image, (x, y))


def button(window, text, x, y, button_width, button_height, idle_color, action_color, action):
    # TODO: use different color when mouse pos is inside button - idle_color and action_color to add
    # TODO: color handling
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(window, (0, 0, 255), (x, y, button_width, button_height))
    text_object(window, text, pygame.font.SysFont("arial", 40), (243, 243, 200), x, y)

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:
        if click[0] == 1:
            action()
