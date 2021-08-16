# Урок 7 Алгоритмы сортировки

# 2. Отсортируйте по возрастанию методом слияния
# одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) > 1:
        middle_point = len(array) // 2
        left_side = array[:middle_point]
        right_side = array[middle_point:]
        # еще раз делим половины, если необходимо
        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                array[k] = left_side[i]
                i += 1
            else:
                array[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            array[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            array[k] = right_side[j]
            j += 1
            k += 1

    return array


if __name__ == "__main__":
    start = 0
    stop = 50
    len_test_array = 11
    test_array = [random.randint(start, stop - 1) for i in range(len_test_array)]
    print(test_array)
    print(merge_sort(test_array))
