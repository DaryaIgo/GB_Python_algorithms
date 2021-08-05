# Урок 4 Эмпирическая оценка алгоритмов на Python

# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile
import timeit
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
    N = 1000
    test_array = [0] * N
    for i in range(N):
        test_array[i] = int(random() * 10)

    print(function_test_1(test_array))
    print(function_test_2(test_array))

    cProfile.run('function_test_1(test_array)')
    cProfile.run('function_test_2(test_array)')

    # N = 1000
    print(timeit.timeit('function_test_1(test_array)', number=100, globals=globals()))  # 0.006278949999796168
    print(timeit.timeit('function_test_2(test_array)', number=100, globals=globals()))  # 0.0027462600000944803
    # N = 10000
    # print(timeit.timeit('function_test_1(test_array)', number=100, globals=globals()))  # 0.09095654000066133
    # print(timeit.timeit('function_test_2(test_array)', number=100, globals=globals()))  # 0.09095654000066133
    # N = 100000
    # print(timeit.timeit('function_test_1(test_array)', number=100, globals=globals()))  # 0.9236457910001263
    # print(timeit.timeit('function_test_2(test_array)', number=100, globals=globals()))  # 0.23173385400059487
    # N = 1000000
    # print(timeit.timeit('function_test_1(test_array)', number=100, globals=globals()))  # 9.371453038999789
    # print(timeit.timeit('function_test_2(test_array)', number=100, globals=globals()))  # 1.401214350000373

    # Сложность алгоритмов O(n)

#          5 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 lesson_4_1.py:14(function_test_1)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          7 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_1.py:20(function_test_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

# N = 1000000
#
#          5 function calls in 0.102 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.102    0.102 <string>:1(<module>)
#         1    0.000    0.000    0.099    0.099 lesson_4_1.py:15(function_test_1)
#         1    0.000    0.000    0.102    0.102 {built-in method builtins.exec}
#         1    0.099    0.099    0.099    0.099 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          7 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#         1    0.000    0.000    0.025    0.025 lesson_4_1.py:21(function_test_2)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#         2    0.024    0.012    0.024    0.012 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 {method 'remove' of 'list' objects}
