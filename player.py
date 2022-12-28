import pygame

pygame.init()


def draw(window, text, font, text_colour, x, y):
    text_image = font.render(text, True, text_colour)
    window.blit(text_image, (x, y))
