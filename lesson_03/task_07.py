"""

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
в том числе написанных самостоятельно.

"""

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

a = array[0]
array_copy = array.copy()
for i in range(len(array)):
    if array[i] < a:
        a = array[i]
array_copy.remove(a)

b = array_copy[0]
for j in range(len(array_copy)):
    if array_copy[j] <= b:
        b = array_copy[j]

print(f"Массив :\n{array}\n Два наименьших элемента : \n[{a}, {b}]")
