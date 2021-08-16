# Урок 7 Алгоритмы сортировки

# 3. Массив размером 2m + 1, где m – натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.
import random
import numpy as np


def median_arr(array):
    array = sorted(array)
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return 0.5 * (array[len(array) // 2 - 1] + array[len(array) // 2])


if __name__ == "__main__":
    start = 0
    stop = 100
    m = 4
    len_test_array = 2 * m + 1
    test_array = [random.randint(start, stop) for i in range(len_test_array)]
    print(test_array)
    print(median_arr(test_array))
    # для проверки
    print(np.median(test_array))
