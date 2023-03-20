import random
import time

# spis1 = [1,2,3]
# spis2 = [4,5,6]
#
#
#
# words = ['verb','noun','spell']
#
# # print(words[])
#
# word = ''
#
# word = words[0]
# # print(word)
# a = len(word)
# # print(a)
# b = list(word)
# # print(b[::-1])
#
# words = words[::-1]
#
# # print(len(words))
#
# text = [str(a),b,words]
#
# # print(len(text))
# d=0
# for i in range(len(text)):
#     print(text[i])
#     d+=len(text[i])
#     print(len(text[i]))
# d = 0
# for i in text:
#     print(i)
#     d+=len(i)
#     print(len(i))
# print(d)
#
# # spis = spis1
# # spis = []
#
# a = 'Nikita'
# b = 'Ryzhov'
# c = a + b
# print(c)
# spis = spis1 + spis2
# print(spis)
# spis = list('Nikita')

# сделать список в котором будеn имя и фамилия(вводится 2-мя строками) посетителя салона связи

# print('')  имя, фамилия и номер ['Никита','Рыжов', 8]

# вывести список в котором имя и фамилия.

# num = 0
# window = {
#     'Окно 1': 'Магазин',
#     'Окно 2': 'Купить сим-карту',
#     'Окно 3': 'Пополнить счет'
# }
# spis1=[]
# while True:
#
#     spis = [input('Введите имя и фамилию: '),input('Введите номер телефона: ')]
#     fl = int(input('Введите номер окна: '))
#     num += 1
#     spis.append(str(num))
#     service = window['Окно ' + str(fl)]
#     spis.append(service)
#
#     print(spis)
#     goon = input('Продолжить работу - введите любой символ: ')
#     if goon:
#         spis1.append(spis)
#         spis = []
#     else:
#         spis1.append(spis)
#         break
# ttime = time.gmtime()
# for name in spis1:
#     print(f'{name} - {ttime}')

# 25.02.2023 13:45

# import random
# def generate_password(number_of_symbols):
#     symbols = []
#     for i in range(number_of_symbols):
#         num = random.randint(1, 3)
#         if num == 1:
#             symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
#         elif num == 2:
#             symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#         elif num == 3:
#             symbols.append(random.choice('0123456789'))
#     password = ''
#     for s in symbols:
#         password += s
#     return password
#
# passw = generate_password(10)

# print(passw)


# deals = [
# 'погулять с друзьями',
# 'почитать новости и сцепиться с кем-нибудь в комментах',
# 'почитать книжку',
# 'рассмотреть потолок',
# 'поиграть в Brawl stars',
# 'помыть посуду',
# 'сказать родителям, что заболел',
# 'залипнуть в летсплеях по роблоксу'
# ]
#
# # # Напиши решение тут
# i = 1
# for deal in deals:
#     print(f'{i}. {deal}')
#     i += 1
#
# print("Какой пункт меню вы хотите добавить?")
# str = input()
#
# deals.append(str)
# i =1
# for deal in deals:
#     print(f'{i}. {deal}')
#     i += 1
#
# print("Какой пункт меню вы хотите заменить?")
# str = int(input())
#
# deals[str] = input('Введите новое значение!')
# for deal in deals:
#     print(f'{i}. {deal}')
#     i += 1
#
#
#
# print("Какой пункт меню вы хотите удалить?")
#
# str = int(input())
#
# deals.pop(str)
#
# for deal in deals:
#     print(f'{i}. {deal}')
#     i += 1
#
#
#
# # for i in range(5):
# #     print(f'{i+1}. Hello Sasha!')
# #
# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0'
# }
#
# # Напиши код тут
# a = input('введите имя')
# b = input('введите номер')
# if a and b:
#     book_phones[a] = b
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
# elif a in book_phones:
#     print(book_phones[a])
# else:
#     print('Нет в телефонной книге')
# spis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dictio = {1: 2,
#           3: 4,
#           7: 8}
# strt = '123.456789'
# index = 8
# print(strt[index])
# print(spis[index])
# print(dictio[index])


shop = {
    'Iphone 14': '300.000р.',
    'Laptop Lenovo 18" 32G': '120.000р.',
    'Ipad 8 pro': '150.000р.',
    'PlayStation 5': '220.000р.',
    'Joystick DualSense PS5': '10.000р.'
}

simnum = {
    'Gold': '+7 777 333 777',
    'Diamond': '+7 777 888 888',
    'Silver': '+7 111 444 444',
    'Bronze': '+7 321 321 321'
}

import time

num = 0
window = {
    'Окно 1': 'Магазин',
    'Окно 2': 'Купить сим-карту',
    'Окно 3': 'Пополнить счет'
}
spis1 = []
while True:

    spis = [input('Введите имя и фамилию: '), input('Введите номер телефона: ')]
    fl = int(input('Введите номер окна: '))
    num += 1
    spis.append(str(num))
    service = window['Окно ' + str(fl)]
    spis.append(service)

    print(spis)
    if fl == 1:
        a = 0
        print('Витрина магазина для покупки, сделайте выбор!')
        for name in shop:
            a001 = str(a) + '001'
            print(f'{a001} - {name} - {shop[name]}')
            a+=1

        uch = input('Введите название или артикул: ')
        for name in shop:
            if name == uch or a001 == uch:
                spis.append(name)
                spis.append(shop[name])



    if fl == 2:
        print('Введите номер или услугу Bronze, Gold, Diamond, Silver')
        cho = input('Ваш выбор: ')
        if cho == 'Bronze' or cho == 'Gold' or cho == 'Diamond' or cho == 'Silver':
            spis.append(simnum[cho])
        else:
            spis.append(cho)
        afs = input('Пополнить счет? да/нет: ')
        if afs == 'да':
            popa = input('Введите сумму: ')
            spis.append(popa)
        elif afs == 'нет':
            print('Продолжить работу - введите любой символ: ')
    if fl == 3:
        afs = input('Пополнить счет? да/нет: ')
        if afs == 'да':
            popa = input('Введите сумму: ')
            spis.append(popa)
        elif afs == 'нет':
            print('Продолжить работу - введите любой символ: ')

    goon = input('Продолжить работу - введите любой символ: ')
    if goon:
        spis1.append(spis)
        spis = []

    else:
        spis1.append(spis)
        break
ttime = time.asctime()
for name in spis1:
    print(f'{name} - {ttime}')
