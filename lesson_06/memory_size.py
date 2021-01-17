from sys import getsizeof

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
 
Для анализа возьмите любые 1-3 ваших программы
или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

"""


def show_me_memory_size(obj, id_set):
    if id(obj) in id_set:
        return 0

    result = getsizeof(obj)
    id_set.add(id(obj))

    if isinstance(obj, (str, int, float, bool)):
        return result

    if isinstance(obj, dict):
        return result + sum(
            show_me_memory_size(key, id_set) + show_me_memory_size(value, id_set)
            for key, value in obj.items()
        )

    if isinstance(obj, (list, tuple, set, frozenset)):
        return result + sum(show_me_memory_size(item, id_set) for item in obj)

    return result


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


result = double_for_count(empty_list, FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)


# for idx, num in enumerate(result, start=START_DIGIT):
#     print(f'{num} чисел кратно {idx}')

#  вариант 2 со словарем:
def dict_count(range_end, bound_start, bound_end):
    result_dict = {}

    for elm in range(bound_start, bound_end + 1):
        result_dict[elm] = range_end // elm

    return result_dict


result_2 = dict_count(TO_NUM, START_DIGIT, END_DIGIT)


#  вариант 3 с генератором:
def gen_count(range_start, range_end, bound_start, bound_end):
    for i in range(range_start, range_end + 1):
        result = 0
        for j in range(bound_start, bound_end + 1):
            if i % j == 0:
                result += 1
    yield f'{result} чисел кратно {i}'


result_3 = gen_count(FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)
# for elm in result_3:
#     print(elm)


memory_sum = [FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT, empty_list]
memory_sum_with_result = show_me_memory_size(memory_sum, set()) + show_me_memory_size(result, set())
memory_sum_with_result_2 = show_me_memory_size(memory_sum, set()) + show_me_memory_size(result_2, set())
memory_sum_with_result_3 = show_me_memory_size(memory_sum, set()) + show_me_memory_size(result_3, set())

print(f'Задействовано памяти для первого варианта: {memory_sum_with_result} bytes', end='\n\n')
print(f'Задействовано памяти для второго варианта: {memory_sum_with_result_2} bytes', end='\n\n')
print(f'Задействовано памяти для третьего варианта: {memory_sum_with_result_3} bytes')

"""
    Задействовано памяти для первого варианта: 868 bytes
    при этом скорость выполнения вразы ниже чем в остальных двух выриантах
    
    Задействовано памяти для второго варианта: 1332 bytes
    при этом скорость выполнения существенно выше чем в предыдущем вырианте
    
    Задействовано памяти для третьего варианта: 636 bytes
    при этом скорость выполнения гараздо выше чем в остальных двух выриантах
    наиболее оптимальная реализация из трех представленных

Интерпретатор Python 3.8, macOS 10.13.6 High Sierra x64

"""
