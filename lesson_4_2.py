# Урок 4 Эмпирическая оценка алгоритмов на Python

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#       Без использования Решета Эратосфена;
#       Использовать алгоритм решето Эратосфена
# Примечание ко всему практическому заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


def sieve_of_Eratosthenes(n):
    list_n = [0] * n
    for i in range(n):
        list_n[i] = i

    list_n[1] = 0

    m = 2
    while m < n:
        if list_n[m] != 0:
            j = m * 2
            while j < n:
                list_n[j] = 0
                j = j + m
        m += 1

    list_test = []
    for i in list_n:
        if list_n[i] != 0:
            list_test.append(list_n[i])

    del list_n
    return list_test


def not_Eratosthenes(n):
    list_n = []
    for i in range(2, n + 1):
        for j in list_n:
            if i % j == 0:
                break
        else:
            list_n.append(i)
    return list_n


if __name__ == "__main__":
    print(sieve_of_Eratosthenes(100))
    print(not_Eratosthenes(100))
    cProfile.run('sieve_of_Eratosthenes(1000)')
    cProfile.run('sieve_of_Eratosthenes(100000)')
    cProfile.run('not_Eratosthenes(1000)')
    cProfile.run('not_Eratosthenes(100000)')

# "Решето Эратосфена" чуть медленней, чем перебор
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#          172 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 lesson_4_2.py:13(sieve_of_Eratosthenes)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          9596 function calls in 0.079 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.079    0.079 <string>:1(<module>)
#         1    0.062    0.062    0.078    0.078 lesson_4_2.py:13(sieve_of_Eratosthenes)
#         1    0.000    0.000    0.079    0.079 {built-in method builtins.exec}
#      9592    0.016    0.000    0.016    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          172 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 lesson_4_2.py:38(not_Eratosthenes)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          9596 function calls in 2.474 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.474    2.474 <string>:1(<module>)
#         1    2.460    2.460    2.474    2.474 lesson_4_2.py:38(not_Eratosthenes)
#         1    0.000    0.000    2.474    2.474 {built-in method builtins.exec}
#      9592    0.014    0.000    0.014    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
