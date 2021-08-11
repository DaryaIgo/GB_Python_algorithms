# Урок 6 Работа с динамической памятью


# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для
# одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
# комментариях версию Python и разрядность вашей ОС.

import sys
# import platform

# print(sys.platform)
# print(platform.architecture())
# print(sys.version)

# linux
# ('64bit', 'ELF')
# 3.8.10  (ver Python)

# Урок 4 Эмпирическая оценка алгоритмов на Python

from random import random

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.


def function_test_1(array):
    sort_arr = sorted(array)
    mins_2 = sort_arr[:2]
    return mins_2


def function_test_2(array):
    min1 = min(array)
    array.remove(min1)
    min2 = min(array)
    return min1, min2


if __name__ == "__main__":
    N = 10000
    test_array = [0] * N
    for i in range(N):
        test_array[i] = int(random() * 100)

    print(function_test_1(test_array))
    print(sys.getsizeof(function_test_1(test_array)))
    print(function_test_2(test_array))
    print(sys.getsizeof(function_test_2(test_array)))
    print(sys.getsizeof(test_array))

# [0, 0] - тут вовзращается список, он занимает больший объем, чем кортеж с теми же значениями, что логично
# 72
# (0, 0)
# 56
# 8056 - размер в байтах списка test_array, рависит от размера N
# 8056 при N = 1000
# 80056 при N = 10000
