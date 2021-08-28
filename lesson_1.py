# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import random

digit = int(input('Введите трехзначное число: '))
if 99 < digit < 999:
    digit3 = digit % 10
    digit2 = (digit // 10) % 10
    digit1 = (digit // 100)
    sum_digits = digit1 + digit2 + digit3
    multi_digits = digit1 * digit2 * digit3
    print('Сумма цифр: ', sum_digits)
    print('Произведение цифр: ', multi_digits)

else:
    print('Вы ввели недоходящее число')

# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
#    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

digit_5 = 5
digit_6 = 6

bit_and = digit_5 & digit_6
bit_or = digit_5 | digit_6
bit_xor = digit_5 ^ digit_6

print('AND  5 & 6 = ', bit_and, bin(bit_and))
print('OR   5 | 6 = ', bit_or, bin(bit_or))
print('XOR  5 ^ 6 = ', bit_xor, bin(bit_xor))

new_digit_left = digit_5 << 2
new_digit_right = digit_5 >> 2

print(f'Побитовый сдвиг цифры 5 влево на 2 знака равен {new_digit_left},'
      f' побитовый сдвиг цифры 5 влево на 2 знака вправо равен {new_digit_right}')

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
#    y = kx + b, проходящей через эти точки

x_1 = float(input('Введите x1: '))
y_1 = float(input('Введите y1: '))
x_2 = float(input('Введите x2: '))
y_2 = float(input('Введите y2: '))

k = (y_1 - y_2) / (x_1 - x_2)
b = y_2 - k * x_2

print(f'Уравнение прямой имеет вид: y = {k}x + {b}')

# 4. Написать программу, которая генерирует в указанных пользователем границах
#    случайное целое число,
#    случайное вещественное число,
#    случайный символ.
#    Для каждого из трех случаев пользователь задает свои границы диапазона.
#    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import re
from random import random
from random import randint
from random import uniform

left_border = input('Введите левую границу диапазона: ')
right_border = input('Введите правую границу диапазона: ')

if re.match('[a-zA-z]', left_border):
    left_border = ord(left_border)
    right_border = ord(right_border)
    sign_random = int(random() * (right_border - left_border + 1)) + left_border
    print(chr(sign_random))
elif float(left_border):
    left_border = float(left_border)
    right_border = float(right_border)
    print(uniform(left_border, right_border))
else:
    left_border = int(left_border)
    right_border = int(right_border)
    print(randint(left_border, right_border))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
#    между ними находится букв.

import re

first_letter = input('Введите любую букву из латинского алфавита: ')
second_letter = input('Введите ещё одну любую букву из латинского алфавита: ')

if re.match('[a-zA-Z]', first_letter):
    position_first_let = ord(first_letter) - 96
    position_sec_let = ord(second_letter) - 96
    amount_letters = abs(position_first_let - position_sec_let) - 1
    print(f'\nПервая буква стоит на позиции {position_first_let} в латинском алфавите, \n'
          f'Вторая буква стоит на позиции {position_sec_let}, \n'
          f'{amount_letters} букв(a/ы) расположены между ними')
else:
    print('Вы ввели не букву из латинского алфавита')

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import re

num_letter = input('Введите номер буквы из латинского алфавита (от 1 до 26): ')
if re.match('[1-26]', num_letter):
    position_let_ascii = int(num_letter) + 96
    letter_alf = chr(position_let_ascii)
    print(f'Это буква "{letter_alf}"')
else:
    print('Вы ввели неподходящее число')

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
#    треугольника, составленного из этих отрезков. Если такой треугольник существует, то
#    определить, является ли он разносторонним, равнобедренным или равносторонним.

a_side = int(input('Введите длину стороны a '))
b_side = int(input('Введите длину стороны b '))
c_side = int(input('Введите длину стороны c '))

if a_side != 0 or b_side != 0 or c_side != 0:
    if a_side + b_side >= c_side and a_side + c_side >= b_side and b_side + c_side >= a_side:
        print('Треугольник существует!')
        if a_side == b_side and b_side == c_side:
            print('Треугольник равносторонний')
        elif a_side == b_side or a_side == c_side or c_side == b_side:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Треугольника не существует!')
else:
    print('Треугольника не существует!')

# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = int(input('Введите год: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year} год - високосный')
else:
    print(f'{year} год -  не вискосный')


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного,
#   но меньше другого).

digit_1 = int(input('Введите любое число '))
digit_2 = int(input('Введите любое число '))
digit_3 = int(input('Введите любое число '))

if digit_1 == digit_2 or digit_2 == digit_3 or digit_1 == digit_3:
    print('Не соблюдены условия задачи')
else:
    if digit_1 < digit_2 < digit_3:
        print(f'Среднее число {digit_2}')
    elif digit_2 < digit_1 < digit_3:
        print(f'Среднее число {digit_1}')
    else:
        print(f'Среднее число {digit_3}')
