b = 32
c = 1.8


while True:

    a = input("Привет! Ты хочешь перевести градусы? Выбери F или C: ")

    if a == 'F':
        d = int(input("Введите колличество F: "))
        cs = (d - b) / c
        print(cs)
    elif a == 'C':
        d = int(input("Введите колличество C: "))
        f = (d * c) + b
        print(f)
    elif a == '':
        break
    else:
        print('Не правильный ввод!')
