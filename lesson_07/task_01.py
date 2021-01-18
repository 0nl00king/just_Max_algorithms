"""

Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
 алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
 постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
 улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""
import random


def bubble_sort(arr, order=-1):
    """

    :param arr: одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100)
    :param order: константа определяющая порядок сортировки в соответствии с условием задачи -1
    :return: отсортированый массив
    """
    n = 1
    while n < len(arr):

        if order == -1:

            for i in range(len(arr) - 1, 0, order):
                if arr[i] > arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            n += 1

        elif order == 1:

            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            n += 1

    return arr


SIZE = 10
RANGE_START = -100
array = [random.randrange(RANGE_START, abs(RANGE_START)) for _ in range(SIZE)]

print(f'Unsorted array is:\n\t{array}\n\nSorted array in descending order is:\n\t{bubble_sort(array)}')
