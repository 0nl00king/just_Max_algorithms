"""

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

"""
import random


def merge_sort(arr, start, end):
    def _inner_sort():
        left_part, right_part = arr[start:middle], arr[middle:end]
        key = start
        lp_idx, rp_idx = 0, 0

        while start + lp_idx < middle and middle + rp_idx < end:
            if left_part[lp_idx] <= right_part[rp_idx]:
                arr[key] = left_part[lp_idx]
                lp_idx += 1
            else:
                arr[key] = right_part[rp_idx]
                rp_idx += 1

            key += 1

        if start + lp_idx < middle:
            while key < end:
                arr[key] = left_part[lp_idx]
                lp_idx += 1
                key += 1
        else:
            while key < end:
                arr[key] = right_part[rp_idx]
                rp_idx += 1
                key += 1

    if end - start > 1:
        middle = (start + end) // 2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle, end)
        _inner_sort()


SIZE = 10
RANGE_START = 0
RANGE_STOP = 50
array = [random.uniform(RANGE_START, RANGE_STOP) for _ in range(SIZE)]

SORT_START = 0
SORT_END = len(array)

print(f'Unsorted array is:\n\t{array}\n')
merge_sort(array, SORT_START, SORT_END)
print(f'Sorted array is:\n\t{array}')
