# Урок 7 Алгоритмы сортировки

# Урок 7 Алгоритмы сортировки

# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random


def bubble_sort(array):
    step = 1

    while step < len(array):
        count = 0

        for elem in range(len(array) - 1):
            if array[elem] < array[elem + 1]:
                array[elem], array[elem + 1] = array[elem + 1], array[elem]
                count += 1

        if count == 0:
            break

        step += 1

    return array


if __name__ == "__main__":
    start = -100
    stop = 100
    len_test_array = 10
    test_array = [random.randint(start, stop - 1) for i in range(len_test_array)]
    print(test_array)
    print(bubble_sort(test_array))
