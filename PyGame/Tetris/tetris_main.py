import random

import pygame as pg
from random import choice, randrange
from copy import deepcopy

W, H = 10, 20
TILE = 30
GAME_RES = W * TILE, H * TILE
RES = 900, 650
FPS = 60

pg.init()

sc = pg.display.set_mode(RES)
# game_sc = pg.display.set_mode(GAME_RES)
game_sc = pg.Surface(GAME_RES)
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

field = [[0 for i in range(W)] for j in range(H)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

figure = deepcopy(random.choice(figures))

main_font = pg.font.Font('font/font.ttf', 65)
font = pg.font.Font('font/font.ttf', 45)

title_tetris = main_font.render('TETRIS', True, pg.Color('darkorange'))
title_score = font.render('score:', True, pg.Color('green'))
title_record = font.render('record:', True, pg.Color('purple'))

get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    if figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False

    return True


while True:
    dx, rotate = 0, False
    sc.fill(pg.Color('black'))
    sc.blit(game_sc, (20, 20))
    game_sc.fill(pg.Color('blue'))

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
            elif event.key == pg.K_UP:
                rotate = True
    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
    # move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = pg.Color('white')
                figure = deepcopy(choice(figures))
                anim_limit = 2000
                break

    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

    # check lines
    line, lines = H - 1, 0
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            anim_speed += 3
            lines += 1
    # compute score
    score += scores[lines]

    # draw grid
    [pg.draw.rect(game_sc, (255, 255, 255), i_rect, 1) for i_rect in grid]

    # draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pg.draw.rect(game_sc, pg.Color('yellow'), figure_rect)

    # draw field
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pg.draw.rect(game_sc, col, figure_rect)

    # draw titles
    sc.blit(title_tetris, (485, 0))
    sc.blit(title_score, (485, 550))
    sc.blit(font.render(str(score), True, pg.Color('white')), (650, 550))

    #sc.blit(title_record, (525, 650))
    #sc.blit(font.render(record, True, pg.Color('gold')), (550, 710))

    pg.display.flip()
    clock.tick(FPS)
