# Урок 3. Массивы. Кортежи. Множества. Списки

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

from random import random

N = 10
array_1 = [0] * N
for i in range(N):
    array_1[i] = int(random()*100)
print(array_1)

max_value = max(array_1)
idx_max_value = array_1.index(max_value)
min_value = min(array_1)
idx_min_value = array_1.index(min_value)

sum_elem = 0

if idx_min_value > idx_max_value:
    idx_min_value, idx_max_value = idx_max_value, idx_min_value

for i in range(idx_min_value + 1, idx_max_value):
    sum_elem += array_1[i]

print(f'Сумма элементов между {min_value} и {max_value} равна {sum_elem}')
