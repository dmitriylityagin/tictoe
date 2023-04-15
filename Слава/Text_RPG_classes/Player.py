import random

from Person import Person
from Utils import Utils
from Constants import role
Utils = Utils()


class Player(Person):
    def __init__(self):
        Person.__init__()
        self.set_name()
        self.set_person_class()
        self.set_class_properties()

        self.money = float(random.randint(10, 500))
        self.inventory = ['яблоко', 'меч']

        Utils.go_on()
        print(f"{self.name} - {self.person_class}.")
        print("(～￣▽￣)～ У него такие характеристики:")
        print(f" здоровье - {self.health},\n атака - {self.attack},\n защита - {self.defence}.")
        Utils.go_on()

    def set_name(self):
        while True:
            player_name = input(f'(☞ﾟヮﾟ)☞ Как зовут твоего героя?\n')
            if Utils.is_valid(player_name):
                break

        self.name = player_name

    def set_person_class(self):
        while True:
            choice = input(f"Введи роль: 1-Воин, 2-Лучник, 3-Маг\n")
            if Utils.is_valid(choice, '123'):
                break
        self.person_class = role[choice]

    def increase_money(self, value):
        self.money += value
        print(f"Заработано {value} руб. Осталось: {round(self.money, 2)} руб.")

    def decrease_money(self, value):
        if self.money - value < 0:
            print(f"Герой не может себе этого позволить. (˘･_･˘)")
            return False
        else:
            self.money -= value
            print(f"Потрачено {value} руб. Осталось: {self.money} руб.")
            return True