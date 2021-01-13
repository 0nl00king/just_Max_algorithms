from collections.abc import Mapping, Container
from collections import deque
import sys

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
 
Для анализа возьмите любые 1-3 ваших программы
или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

"""


# def show_me_memory_size(obj, id_set):
#     if id(obj) in id_set:
#         return 0
#
#     result = getsizeof(obj)
#     id_set.add(id(obj))
#
#     if isinstance(obj, str) or isinstance(0, unicode):
#         return result
#
#     if isinstance(obj, Mapping):
#         return result + sum(
#             show_me_memory_size(key, id_set) + show_me_memory_size(value, id_set) for key, value in obj.items())
#
#     if isinstance(obj, Container):
#         return result + sum(show_me_memory_size(item, id_set) for item in obj)
#
#     return result


def deq_container(memory_sum, deq_sum=0):
    for x in memory_sum:
        deq_sum += sys.getsizeof(x)

        if type(x) == str or type(x) == int:
            continue

        elif type(x) == list or type(x) == deque or type(x) == tuple:
            for n in x:
                deq_sum += sys.getsizeof(n)

        elif type(x) == dict:
            for n in x:
                deq_sum += sys.getsizeof(x)
                deq_sum += sys.getsizeof(x[n])

    return deq_sum


# Оценка алгоритмов.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


FROM_NUM = 2
TO_NUM = 99
START_DIGIT = 2
END_DIGIT = 9

empty_list = [0 for _ in range(END_DIGIT - 1)]


#  вариант 1 со списком, через 2 цикла for:
def double_for_count(empty_list, range_start, range_end, bound_start, bound_end):
    for i in range(range_start, range_end + 1):
        for j in range(bound_start, bound_end + 1):
            if i % j == 0:
                empty_list[j - bound_start] += 1
    return empty_list


# result = double_for_count(empty_list, FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)
# for idx, num in enumerate(result, start=START_DIGIT):
#     print(f'{num} чисел кратно {idx}')

#  вариант 2 со словарем:
def dict_count(range_end, bound_start, bound_end):
    result_dict = {}

    for elm in range(bound_start, bound_end + 1):
        result_dict[elm] = range_end // elm

    return result_dict


# print(dict_count(TO_NUM, START_DIGIT, END_DIGIT))


#  вариант 3 с генератором:
def gen_count(range_start, range_end, bound_start, bound_end):
    for i in range(range_start, range_end + 1):
        result = 0
        for j in range(bound_start, bound_end + 1):
            if i % j == 0:
                result += 1
    yield f'{result} чисел кратно {i}'


# p = gen_count(FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)
# for elm in p:
#     print(elm)


memory_sum = deque()
memory_sum.append(FROM_NUM)
memory_sum.append(TO_NUM)
memory_sum.append(START_DIGIT)
memory_sum.append(END_DIGIT)
memory_sum.append(empty_list)


print(f'Задействовано памяти: {deq_container(memory_sum)}')

"""
не успел.....

Интерпретатор Python 3.8, MacOS

"""
