import timeit
import cProfile

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
print(timeit.timeit('double_for_count(empty_list, FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 0.013638090999999998
print(timeit.timeit('double_for_count(empty_list, FROM_NUM, 198, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 0.025389648
print(timeit.timeit('double_for_count(empty_list, FROM_NUM, 396, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 0.044510429
print(timeit.timeit('double_for_count(empty_list, FROM_NUM, 792, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 0.09195057499999999
cProfile.run('double_for_count(empty_list, FROM_NUM, 1_000_000, START_DIGIT, END_DIGIT)')


# 0.013638090999999998
# 0.025389648
# 0.044510429
# 0.09195057499999999
#          4 function calls in 1.190 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.190    1.190 <string>:1(<module>)
#         1    1.190    1.190    1.190    1.190 task_01.py:17(double_for_count)
#         1    0.000    0.000    1.190    1.190 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  вариант 2 со словарем:
def dict_count(range_end, bound_start, bound_end):
    result_dict = {}

    for elm in range(bound_start, bound_end + 1):
        result_dict[elm] = range_end // elm

    return result_dict


# print(dict_count(TO_NUM, START_DIGIT, END_DIGIT))
print(
    timeit.timeit('dict_count(TO_NUM, START_DIGIT, END_DIGIT)', number=100, globals=globals()))  # 0.0001357919999998014
print(timeit.timeit('dict_count(198, START_DIGIT, END_DIGIT)', number=100, globals=globals()))  # 0.00013282800000014028
print(timeit.timeit('dict_count(396, START_DIGIT, END_DIGIT)', number=100, globals=globals()))  # 0.00013310199999994055
print(timeit.timeit('dict_count(792, START_DIGIT, END_DIGIT)', number=100, globals=globals()))  # 0.0001376689999998959
cProfile.run('dict_count(1_000_000, START_DIGIT, END_DIGIT)')


# 0.0001357919999998014
# 0.00013282800000014028
# 0.00013310199999994055
# 0.0001376689999998959
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_01.py:40(dict_count)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

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
print(timeit.timeit('gen_count(FROM_NUM, TO_NUM, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 4.336299999985194e-05
print(timeit.timeit('gen_count(FROM_NUM, 198, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 4.314100000013532e-05
print(timeit.timeit('gen_count(FROM_NUM, 396, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 4.332699999998191e-05
print(timeit.timeit('gen_count(FROM_NUM, 792, START_DIGIT, END_DIGIT)', number=100,
                    globals=globals()))  # 4.28420000000429e-05
cProfile.run('gen_count(FROM_NUM, 1_000_000_000, START_DIGIT, END_DIGIT)')

# 4.336299999985194e-05
# 4.314100000013532e-05
# 4.332699999998191e-05
# 4.28420000000429e-05
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_01.py:58(gen_count)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
