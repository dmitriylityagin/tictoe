import os
import random

clear = lambda: os.system('cls')
print("Поехали!")
clear()
words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)
letters = []


hlth = 10
def hp_run():
        global letter
        letter = input('Введите букву:')
        isWin = True
        letters.append(letter)
        print(letters)
        for symb in word:
            if symb in letters:
                print(symb, end=' ')
            else:
                print('*', end=' ')
                isWin = False
        print()
        clear()
        return isWin
def check_win(hp,isWin = False):
        if isWin:
            print('Ты угадал! Молодец!')
            hp = -1
            return hp
        if letter not in word:
            hp -= 1
            print(f'Осталось попыток: {hp}')
        return hp
while hlth>0:
    fl = hp_run()
    hlth = check_win(hlth,fl)


# def greet():
#     print('Privet Oleg! Welcom to the cofee shop!')
# def dishes(choice = '1'):
#     print(' /------\\')
#     if choice == '1':
#         print(' ⋁ΞΞΞΞΞ⋁')
#     elif choice == '2':
#         print('◯◯◯◯')
#     print(' \______/')
#
# greet()
#
# dishes()