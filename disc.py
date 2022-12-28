import pygame


# JM

class Disc:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.disc_image = None

    def draw(self, window):
        if self.color == 'red':
            self.disc_image = pygame.image.load("red_disc.png")
        elif self.color == 'yellow':
            self.disc_image = pygame.image.load("yellow_disc.png")
        window.blit(pygame.transform.scale(self.disc_image, (110, 110)), (self.x, self.y))
