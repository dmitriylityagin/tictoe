from typing import Any

import pygame as pg
from random import randrange

from pygame.surface import Surface

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }

dx, dy = 0, 0
fps = 40
score = 0
speed_count, snake_speed = 0, 10
game_state = "start_menu"

pg.init()
sc = pg.display.set_mode([RES, RES])
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 25)
font_end = pg.font.SysFont('Arial', 66, bold=True)
img = pg.image.load('1.jpg').convert()


# noinspection PyGlobalUndefined
def init_game():
    global x, y, apple, length, snake, dirs, dx, dy, fps, score
    x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    length = 1
    snake = [(x, y)]
    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }

    dx, dy = 0, 0
    fps = 40
    score = 0


def close_game():
    for act in pg.event.get():
        if act.type == pg.QUIT:
            exit()


def draw_start_menu():
    sc.fill(pg.Color('black'))
    font = pg.font.SysFont('arial', 40)
    title = font.render('Super Spam ™', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    sc.blit(title, (RES / 2 - title.get_width() / 2, RES / 2 - title.get_height() / 2))
    sc.blit(start_button, (RES / 2 - start_button.get_width() / 2, RES / 2 + start_button.get_height() / 2))
    pg.display.update()


def draw_game_over_screen():
    sc.fill((0, 0, 0))
    font = pg.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    sc.blit(title, (RES / 2 - title.get_width() / 2, RES / 2 - title.get_height() / 3))
    sc.blit(restart_button, (RES / 2 - restart_button.get_width() / 2, RES / 1.9 + restart_button.get_height()))
    sc.blit(quit_button, (RES / 2 - quit_button.get_width() / 2, RES / 2 + quit_button.get_height() / 2))
    pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    if game_state == "start_menu":
        draw_start_menu()
        if game_state == "start_menu":
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                init_game()
                game_state = "game"
                game_over = False
    if game_state == "game_over":
        draw_game_over_screen()
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            game_state = "start_menu"
        if keys[pg.K_q]:
            break
    if game_state == "game":
        sc.blit(img, (0, 0))
        # drawing snake, apple
        [pg.draw.rect(sc, pg.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
        pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE, SIZE))
        # Show score
        render_score = font_score.render(f'SCORE: {score}', 1, pg.Color('orange'))
        sc.blit(render_score, (5, 5))
        # snake movement
        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]
        # eating apple
        if snake[-1] == apple:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            length += 1
            score += 1
            fps += 1
            snake_speed -= 1
            snake_speed = max(snake_speed, 4)
        # game over
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            pg.display.flip()
            game_over = True
            game_state = "game_over"
        pg.display.flip()
        clock.tick(fps)
        close_game()
        # control
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
        elif key[pg.K_s]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        elif key[pg.K_a]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        elif key[pg.K_d]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
        elif key[pg.K_q]:
            pg.quit()
pg.quit()