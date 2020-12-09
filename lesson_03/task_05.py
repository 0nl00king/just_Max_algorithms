"""

В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
в том числе написанных самостоятельно.

"""

import random

SIZE = 20
MIN_ITEM = - 999
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_values = []
for i in range(len(array)):
    if array[i] < 0:
        min_values.append(array[i])
smallest = min_values[0]

for j in range(len(min_values)):
    if min_values[j] > smallest:
        smallest = min_values[j]

idx = array.index(smallest, 0, len(array))

print(f"Массив :\n{array} \nМаксимальное отрицательное число :\n{smallest}, имеет индекс {idx}")
