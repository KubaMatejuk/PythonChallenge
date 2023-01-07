import pygame


def select_column_by_key(keys):
    if keys[pygame.K_1]:
        return 1
    elif keys[pygame.K_2]:
        return 2
    elif keys[pygame.K_3]:
        return 3
    elif keys[pygame.K_4]:
        return 4
    elif keys[pygame.K_5]:
        return 5
    elif keys[pygame.K_6]:
        return 6
    elif keys[pygame.K_7]:
        return 7


# MMI
def select_column_by_mouse(mouse_tick):
    pass
