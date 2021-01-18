"""

Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
 в одной находятся элементы, которые не меньше медианы,
 в другой — не больше медианы.

Примечание:
 задачу можно решить без сортировки исходного массива.
 Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
  (сортировка слиянием также недопустима).

"""
import random


def gnome_sort(arr):
    idx, arr_len = 0, len(arr)

    while idx < arr_len:
        if idx == 0:
            idx += 1

        if arr[idx] >= arr[idx - 1]:
            idx += 1
        else:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1

    return arr


def median(arr):
    arr_len = len(arr)

    if arr_len < 1:
        return None

    if arr_len % 2 == 1:
        return gnome_sort(arr)[arr_len // 2]
    else:
        return sum(gnome_sort(arr)[arr_len // 2 - 1:arr_len // 2 + 1]) / 2


SIZE = 5
RANGE_START = -100
array = [random.randrange(RANGE_START, abs(RANGE_START)) for _ in range(2 * SIZE + 1)]

print(
    f'Unsorted array is:\n\t{array}\n\nSorted array is:\n\t{gnome_sort(array)}\n\nMedian of array is:\n\t{median(array)}')
