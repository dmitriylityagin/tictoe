from ursina import *
import random
import math

app = Ursina()

camera.orthographic = True
camera.fov = 25

Entity(
    model='quad',
    texture="assets/street.png",
    scale=60,
    z=1,
)

player = Entity()
anim = Animator(animations={'idle': Entity(parent=player, model='cube', texture='player.png')})

npcs = []

for i in range(12):
    if i < 6:
        rot = 180
        val = -1
    else:
        rot = 0
        val = 1
    npc = Entity(model='cube', texture='assets/npc.png', rotation=rot,
                 position=(random.randint(-15, 10), random.randint(-15, 10)), collider='box', tag='npc')
    # follow = SmoothFollow(target=player, speed=8, offset=[2, 2, 0])
    # npc.add_script(follow)
    npcs.append((npc, val))

for i in [-10, 10]:
    for j in [-8, 8]:
        Sprite(model='cube', texture='assets/house.png', scale=3, collider='box', position=(i, j, 0),
               rotation_z=0 if i == 4 else 180, tag='house')
for i in [-5.5, 5]:
    for j in [-15, 15]:
        Sprite(model='cube', texture='assets/house.png', scale=3, collider='box', position=(i, j, 0),
               rotation_z=270 if i == 2.5 else 90, tag='house')

car = Entity(model='quad', texture='assets/au.png', collider='box', scale=(4, 2), y=10, tag='car')
car_mode = False


def input(key):
    global car_mode

    if key == 'left mouse down':
        if not car_mode:
            x, y, z = mouse.position
            real_pos = player.position + (x * camera.fov, y * camera.fov, 0)
            direction = [real_pos[0] - player.x, real_pos[1] - player.y, 0]
            dot = Entity(model='sphere', color=color.black, scale=0.8, position=player.position, collider='sphere',
                         tag='bullet')
            dot.animate_position(player.position + [3 * p for p in direction], duration=0.5, curve=curve.linear)
            player.rotation_z = 450 - math.degrees(math.atan2(direction[1], direction[0]))
            invoke(destroy, dot, delay=0.5)
            shoot = raycast(player.position, direction, distance=10, ignore=(player, dot), debug=True)
            if shoot.hit and shoot.entity.tag == 'npc':
                Entity(model='quad', texture='assets/npc_dead.png', color=color.random_color(), scale=0.7,
                       position=shoot.entity.position)
                shoot.entity.disable()


def update():
    global car_mode
    if car_mode:
        head_ray = raycast(car.position, (math.cos(math.radians(360 - car.rotation_z)),
                                          math.sin(math.radians(360 - car.rotation_z)), 0),
                           ignore=(car,), distance=1.5)
        if head_ray.hit and head_ray.entity.tag == 'npc':
            Entity(model='quad', texture='assets/npc_dead.png', color=color.random_color(), scale=0.7,
                   position=head_ray.entity.position)
            head_ray.entity.disable()

        back_ray = raycast(car.position, (-1 * math.cos(math.radians(360 - car.rotation_z)),
                                          -1 * math.sin(math.radians(360 - car.rotation_z)), 0),
                           ignore=(car,), distance=1.5)
        if back_ray.hit and back_ray.entity.tag == 'npc':
            Entity(model='quad', texture='assets/npc_dead.png', color=color.random_color(), scale=0.7,
                   position=back_ray.entity.position)
            back_ray.entity.disable()

    for npc, val in npcs:
        npc.y += 3 * time.dt
        if val == 1:
            if npc.y > 22:
                npc.y = -22
        else:
            if npc.y < 22:
                npc.y = -22

    #     car.x -= held_keys['a'] * 5 * time.dt
    #     car.x += held_keys['d'] * 5 * time.dt

    player.y += held_keys['w'] * 5 * time.dt
    player.y -= held_keys['s'] * 5 * time.dt
    player.x += held_keys['d'] * 5 * time.dt
    player.x -= held_keys['a'] * 5 * time.dt

    if held_keys['w']:
        player.rotation_z = -90

    if held_keys['d']:
        player.rotation_z = 360

    if held_keys['a']:
        player.rotation_z = 180

    if held_keys['s']:
        player.rotation_z = 90

    if held_keys['w'] and held_keys['d']:
        player.rotation_z = -45

    if held_keys['w'] and held_keys['a']:
        player.rotation_z = -125

    if held_keys['s'] and held_keys['d']:
        player.rotation_z = 45

    if held_keys['s'] and held_keys['a']:
        player.rotation_z = 125

    camera.position = player.position + [0, 0, -4]


# здесь будет описана игровая логика

app.run()
