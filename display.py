import pygame


def text_object(window, text, font, text_colour, x, y):
    text_image = font.render(text, True, text_colour)
    window.blit(text_image, (x, y))


def button(window, text, x, y, button_width, button_height, button_idle_color, button_action_color, text_idle_color,
           text_action_color, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_center = (x+button_width/2, y+button_height/2)
    font = pygame.font.SysFont("arial", int(button_height * 0.8))

    pygame.draw.rect(window, button_idle_color, (x, y, button_width, button_height))
    text_surface, text_surface_rect = get_button_rectangle(text, font, text_idle_color)
    text_surface_rect.center = button_center
    window.blit(text_surface, text_surface_rect)

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:
        pygame.draw.rect(window, button_action_color, (x, y, button_width, button_height))
        text_surface, text_surface_rect = get_button_rectangle(text, font, text_idle_color)
        text_surface_rect.center = button_center
        window.blit(text_surface, text_surface_rect)
        if click[0] == 1:
            action()


def get_button_rectangle(text, font, text_colour):
    text_surface = font.render(text, True, text_colour)
    return text_surface, text_surface.get_rect()
