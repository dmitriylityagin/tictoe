import pygame
from pygame.time import Clock
import colors
import config

pygame.init()
screen = pygame.display.set_mode((config.screen_height, config.screen_width))
clock: Clock = pygame.time.Clock()
background_image = pygame.image.load('images/bg.png')

while True:
    screen.fill(colors.GREENYELLOW)
    # screen.blit(background_image, (0, 0)
    pygame.display.update()
    clock.tick(60)


