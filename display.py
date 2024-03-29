import pygame


def text_object(window, text, font, text_colour, x, y):
    """
    Creates and displays text object on the screen

    :param window: pygame.display screen
    :param text: parameter of displayed text: content
    :param font: parameter of displayed text: content font
    :param text_colour: parameter of displayed text: content color
    :param x: x_coord of desired center of a text object
    :param y: y_coord of desired center of a text object
    """
    text_surface, text_surface_rect = get_text_rectangle(text, font, text_colour)  # Surface and Rect objects
    text_surface_rect.center = (x, y)  # overwrite center coordinates of text object
    window.blit(text_surface, text_surface_rect)


def button(window, text, x, y, button_width, button_height, button_idle_color, button_action_color, text_idle_color,
           text_action_color, action):
    """
    Creates and displays a button in the menu

    :param window: pygame.display screen
    :param text: parameter of displayed text: content
    :param x: x_coord of the left top corner of button rectangular shape
    :param y: y_coord of the left top corner of button rectangular shape
    :param button_width: button width
    :param button_height: button height
    :param button_idle_color: button's primary color
    :param button_action_color: button's secondary color (hover color)
    :param text_idle_color: the primary color of the text on the button
    :param text_action_color: the secondary color of the text on the button (hover text color)
    :param action: function when button is pressed
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_center = (x+button_width/2, y+button_height/2)  # create the center of a rectangular object
    font = pygame.font.SysFont("arial", int(button_height * 0.8))

    pygame.draw.rect(window, button_idle_color, (x, y, button_width, button_height))
    text_surface, text_surface_rect = get_text_rectangle(text, font, text_idle_color)  # Surface and Rect objects
    text_surface_rect.center = button_center  # overwrite center coordinates of text object
    window.blit(text_surface, text_surface_rect)

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:  # hover effect conditions
        pygame.draw.rect(window, button_action_color, (x, y, button_width, button_height))
        text_surface, text_surface_rect = get_text_rectangle(text, font, text_action_color)
        text_surface_rect.center = button_center
        window.blit(text_surface, text_surface_rect)
        if click[0] == 1:
            action()


def get_text_rectangle(text, font, text_colour):
    """
    Creates a new Surface object with specified text, font and text color. Returns Surface object and Rect object
    with dimensions of covering the entire Surface
    """
    text_surface = font.render(text, True, text_colour)
    return text_surface, text_surface.get_rect()
