import pygame as pg
from random import choice, randrange
from copy import deepcopy

W, H = 10, 20
TILE = 35
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60

pg.init()
game_sc = pg.display.set_mode(GAME_RES)
# game_sc = pg.Surface(GAME_RES)
clock = pg.time.Clock()

grid = [pg.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pg.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pg.Rect(0, 0, TILE - 2, TILE - 2)

anim_count, anim_speed, anim_limit = 0, 60, 2000

figure = deepcopy(figures[3])

def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    if figure[i].y > H - 1:
        return False

    return True


while True:
    dx = 0
    game_sc.fill(pg.Color('green'))


    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dx = -1
            elif event.key == pg.K_RIGHT:
                dx = 1
            elif event.key == pg.K_DOWN:
                anim_limit = 100
    #move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
    #move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                figure = deepcopy(figure_old)
                anim_limit = 2000
                break

    #draw grid
    [pg.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    #draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pg.draw.rect(game_sc, pg.Color('white'), figure_rect)
    pg.display.flip()
    clock.tick(FPS)
