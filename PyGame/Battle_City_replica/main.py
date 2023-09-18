import pygame as pg
from class_tank import *

size = (1280, 1024)
screen = pg.display.set_mode(size)
FPS = pg.time.Clock()

player = Tank()
player.rect.topleft = (size[0] // 4, size[1] // 2)
player2 = Tank2()
player2.rect.topleft = (size[0] // 4 * 3, size[1] // 2)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    player.update(screen)
    player2.update(screen)
    FPS.tick(60)
    pg.display.update()