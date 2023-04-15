import time
from Constants import classes


class Person:
    def __init__(self):
        self.name = ''
        self.person_class = ''
        self.health = 0
        self.attack = 0
        self.defence = 0
        self.skills = {}
        self.is_alive = True
        self.max_health = self.health

    def set_class_properties(self):
        self.health = classes[self.person_class]['здоровье']
        self.attack = classes[self.person_class]['атака']
        self.defence = classes[self.person_class]['защита']
        self.skills = classes[self.person_class]['навыки']

    def attack_enemy(self, enemy1, enemy2):
        print(f"{enemy1.name} атакует {enemy2.name}!")
        time.sleep(2)

        damage = enemy1.attack - enemy2.defence
        if damage < 0: damage = 1
        enemy2.health -= damage

        print(
            f"{enemy1.name} наносит {damage} урона и у {enemy2.name} остается {enemy2.health} здоровья!")
        time.sleep(2)

    def fight_for_the_win(self, attacker, defender):
            while attacker.is_alive and defender.is_alive:
                time.sleep(2)

                if attacker.health > 0:
                    self.attack_enemy(attacker, defender)
                else:
                    print(f"{attacker.name} потерпел поражение!")
                    attacker.is_alive = False
                    return False

                if defender.health > 0:
                    self.attack_enemy(defender, attacker)
                else:
                    print(f"{defender.name} потерпел поражение!")
                    defender.is_alive = False
                    return True