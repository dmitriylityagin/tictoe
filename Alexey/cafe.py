import time

def greet(name):
    print(f'Privet {name}! Welcom to the cofee shop!')

def dishes(choise='2'):
    print(' /------\\')
    if choise =='1':
        print('  V====V')
    elif choise == '2':
        print('  oooooo')
    print(' \______/')

client_list=[]
for i in range(16):
    client_list.append(True)

def submit_order(num, choise):
    order_list = {}
    name = input('введите имя! ')
    phone = input('введите номер телефона! ')
    ttime = time.asctime()
    order_list[num] = [name, phone, choise, ttime]
    return order_list

def resevartion(order_num: int):
    #написать условную конструкцию, которая позволит нам проверить текущий статус бронирования
    global client_list
    client_list[order_num]=False
    print(client_list)

greet("Алексей")
dishes()

while True:
    a = int(input('Номер столика?'))
    resevartion(a-1)
    b = input('Заказ из меню: (номер блюда)')
    dishes(b)
    res = submit_order(a, b)
    print(res)



    # def greet(name):
    #     print(f'Privet {name}! Welcom to the cofee shop!')
    #
    #
    # def dishes(choice='1'):
    #     print(' /------\\')
    #     if choice == '1':
    #         print(' ⋁ΞΞΞΞΞ⋁')
    #     elif choice == '2':
    #         print('◯◯◯◯')
    #     print(' \______/')
    #
    #
    # client_list = []
    # for i in range(16):
    #     client_list.append(True)
    #
    #
    # # print(client_list)
    # # надо дописать условие для проверки списка бронирования, и если столик занят, то вывести сообщение об этом пользователю. Столик с номером 10 занят, пож-та введите другое число.
    # def resevartion(order_num: int):
    #     global client_list
    #
    #     client_list[order_num] = False
    #     print(client_list)
    #
    #
    # greet("Алексей")
    # dishes()
    # while True:
    #     a = int(input('Введите номер столика: '))
    #     resevartion(a - 1)