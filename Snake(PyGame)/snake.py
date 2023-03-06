import pygame as pg
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }

dx, dy = 0, 0
fps = 5

pg.init()
sc = pg.display.set_mode()
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 25)

while True:
    sc.fill(pg.Color('black'))
    # drawing snake, apple
    [(pg.draw.rect(sc, pg.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE, SIZE))
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        break
    if len(snake) != len(set(snake)):
        break
    pg.display.flip()
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # control
    key = pg.key.get_pressed()
    if key[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    if key[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    if key[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    if key[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
