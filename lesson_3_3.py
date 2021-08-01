# Урок 3. Массивы. Кортежи. Множества. Списки

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 10
array_1 = [0] * N
for i in range(N):
    array_1[i] = int(random()*100)

max_value = max(array_1)
idx_max_value = array_1.index(max_value)
min_value = min(array_1)
idx_min_value = array_1.index(min_value)

print(f'До замены: {array_1}\n'
      f'Максимальное значение {max_value} индекс {idx_max_value}\n'
      f'Минимальное значение {min_value} индекс {idx_min_value}')

array_1[idx_min_value], array_1[idx_max_value] = array_1[idx_max_value], array_1[idx_min_value]
print(f'После заммены {array_1}')
