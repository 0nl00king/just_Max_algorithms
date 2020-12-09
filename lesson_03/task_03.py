"""

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
в том числе написанных самостоятельно.

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_idx, max_idx = 0, 0

for i in range(len(array)):
    if array[i] > array[max_idx]:
        max_idx = i
    elif array[i] < array[min_idx]:
        min_idx = i

print(f'Исходный массив :\n{array}')

array[max_idx], array[min_idx] = array[min_idx], array[max_idx]
print(f'Массив после обмена максимального и минимального значения местами:\n{array}')
