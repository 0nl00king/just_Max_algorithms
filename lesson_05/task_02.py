"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
 (пусть это и не очевидно с первого раза. Вы же не Голландец ;-).
"""

from collections import deque

BASE = 16

HEX_NUMBERS = ('0', '1',
               '2', '3',
               '4', '5',
               '6', '7',
               '8', '9',
               'A', 'B',
               'C', 'D',
               'E', 'F')

HEX_TO_DEC_DICT = {'0': 0, '1': 1,
                   '2': 2, '3': 3,
                   '4': 4, '5': 5,
                   '6': 6, '7': 7,
                   '8': 8, '9': 9,
                   'A': 10, 'B': 11,
                   'C': 12, 'D': 13,
                   'E': 14, 'F': 15}


def sum_hex_with_deque(first_deque, second_deque):
    first_deque, second_deque = first_deque.copy(), second_deque.copy()

    if len(second_deque) > len(first_deque):
        first_deque, second_deque = second_deque, first_deque

    second_deque.extendleft('0' * (len(first_deque) - len(second_deque)))

    result = deque()
    in_mind = 0
    while len(first_deque) != 0:
        first_hex = HEX_TO_DEC_DICT[first_deque.pop()]
        second_hex = HEX_TO_DEC_DICT[second_deque.pop()]
        result_number = first_hex + second_hex + in_mind

        if result_number >= BASE:
            in_mind = 1
            result_number -= BASE
        else:
            in_mind = 0

        result.append(HEX_NUMBERS[result_number])

    if in_mind == 1:
        result.appendleft('1')

    return result


def mul_hex_with_deque(first_deque, second_deque):
    first_deque, second_deque = first_deque.copy(), second_deque.copy()

    if len(second_deque) > len(first_deque):
        first_deque, second_deque = second_deque, first_deque

    second_deque.extendleft('0' * (len(first_deque) - len(second_deque)))
    result = deque('0')

    while len(second_deque) != 0:

        second_hex = HEX_TO_DEC_DICT[second_deque.pop()]

        tmp = deque('0')
        for _ in range(second_hex):
            tmp = sum_hex_with_deque(tmp, first_deque)

        tmp.extend('0' * (len(first_deque) - len(second_deque) - 1))

        result = sum_hex_with_deque(result, tmp)

    return result


a = deque(input('Введите первое шеснадцатиричное число :\n').upper())
b = deque(input('Введите второе шеснадцатиричное число :\n').upper())

print(f'{list(a)} + {list(b)} = {list(sum_hex_with_deque(a, b))}')
print(f'{list(a)} * {list(b)} = {list(mul_hex_with_deque(a, b))}')

# def dec_from_hex_dict(n):
#     return {'0': 0, '1': 1,
#             '2': 2, '3': 3,
#             '4': 4, '5': 5,
#             '6': 6, '7': 7,
#             '8': 8, '9': 9,
#             'A': 10, 'B': 11,
#             'C': 12, 'D': 13,
#             'E': 14, 'F': 15}[n]
