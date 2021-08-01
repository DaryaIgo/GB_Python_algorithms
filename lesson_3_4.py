# Урок 3. Массивы. Кортежи. Множества. Списки

# 4. Определить, какое число в массиве встречается чаще всего.

from random import random

N = 50
array_1 = [0] * N
for i in range(N):
    array_1[i] = int(random()*100)
print(array_1)

digit = array_1[0]
max_frequency = 1

for i in range(N - 1):
    frequency = 1
    for j in range(i + 1, N):
        if array_1[i] == array_1[j]:
            frequency += 1
    if frequency > max_frequency:
        max_frequency = frequency
        digit = array_1[i]

print(f'Число {digit} встречается {max_frequency} раз(а)')
