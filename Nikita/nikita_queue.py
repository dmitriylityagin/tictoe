'''написать условную конструкцию, если число людей четное,
 то нужно разделить посетителей на 2 половины,
 и вывести на экран два списка - до обеда, после обеда.
  если число не четное, то оставить большую половину до обеда,
  а меньшую после обеда. так же если посетителей больше 20 человек,
   то отправить часть на следующий день.
 обед 12.30 завершение работы 17.30 начало 9.00 на одного клиента 30 минут.
 2 часа работают 2 окна.'''

queue = int(input('Сколько посетителей зарегестрировалось: '))
lan = 20
if queue % 2 == 0:
    if queue <= 20:
        print(f'{int(queue / 2)}- Людей до обеда и после обеда.')
        re = queue / 2
        if re <= 8 and re % 2 == 0:
            print(f'{int(re/2)} - в окно 1,2')
        elif re <= 8 and re % 2 != 0:
            sum1 = int(re / 2)
            print(f'{sum1} - в окно 1, {sum1+1} - в окно 2')
        else:
            sum1 = int(re - 8)
            print(f'{int(8 / 2)} - в окно 1,2 и {sum1} в окно 1 после 11.00')
    else:
        re = queue - lan
        print(f'{int(lan / 2)}- Людей до обеда и после обеда, {re}- Людей на следущий день.')
if queue % 2 != 0:
    if queue < 20:
        re2 = queue // 2
        re1 = queue - re2
        print(f'{re2}- Людей до обеда, {re1}- Людей после обеда.')
    else:
        re = queue - lan
        print(f'{int(lan / 2)}- Людей до обеда и после обеда, {re}- Людей на следущий день.')