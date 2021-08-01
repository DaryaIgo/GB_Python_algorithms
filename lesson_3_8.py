# Урок 3. Массивы. Кортежи. Множества. Списки

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

column = 5
row = 4
matrix = []
for i in range(row):
    sum_column = []
    s = 0
    for j in range(column - 1):
        n = int(input('Введите значение: '))
        s += n
        sum_column.append(n)
    sum_column.append(s)
    matrix.append(sum_column)
    print(f' {sum_column}')


for i in matrix:
    print(i)
