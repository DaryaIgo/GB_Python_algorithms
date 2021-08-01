# Урок 3. Массивы. Кортежи. Множества. Списки

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

N = 50
array_1 = [0] * N
for i in range(N):
    # решила так заполнить массив, чтобы еще и отрицательные значения рандомные были
    array_1[i] = int(random()*100) - int(random()*100)
print(array_1)

array_2 = []
for i in range(N):
    if array_1[i] < 0:
        array_2.append(array_1[i])

sort_array_2 = sorted(array_2)
print(sort_array_2)
print(f'Максимлаьный отрицательный элемент равен {sort_array_2[-1]}')
