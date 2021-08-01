# Урок 3. Массивы. Кортежи. Множества. Списки

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

column = 10
row = 10
matrix = [[int(random()*10)] * row for i in range(column)]

for i in range(column):
    for j in range(row):
        matrix[i][j] = int(random()*10)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

res = (max(min(i) for i in matrix))
print(f'Максимальный элемент среди минимальных: {res}')
