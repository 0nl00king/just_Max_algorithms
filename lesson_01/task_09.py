"""

Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).

"""

print('Введите три разных числа :')
first = float(input('Первое число = '))
second = float(input('Первое число = '))
third = float(input('Первое число = '))

if second < first < third or third < first < second:
    print(f'{first:.2f} - среднее.')
elif first < second < third or third < second < first:
    print(f'{second:.2f} - среднее.')
else:
    print(f'{third:.2f} - среднее.')
