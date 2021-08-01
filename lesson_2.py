# Урок 2. Циклы. Рекурсия. Функции.

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

sign = input('Введите знак операции (для выхода из программы введите 0): ')

while sign != '0':
    if sign != '+' and sign != '-' and sign != '/' and sign != '*':
        sign = input('Введите знак операции (для выхода из программы введите 0): ')
        print('Вы ввели неправильный знак')
    break


while sign != '0':
    digit_1 = int(input('Введите первое число: '))
    digit_2 = int(input('Введите второе число: '))
    sign = input('Введите знак операции (для выхода из программы введите 0): ')
    result = 0
    if sign == '+':
        result = digit_1 + digit_2
        if digit_2 < 0:
            print(f'{digit_1} + ({digit_2}) = {result}')
        else:
            print(f'{digit_1} + {digit_2} = {result}')
    elif sign == '-':
        result = digit_1 - digit_2
        if digit_2 < 0:
            print(f'{digit_1} - ({digit_2}) = {result}')
        else:
            print(f'{digit_1} - {digit_2} = {result}')
    elif sign == '*':
        result = digit_1 * digit_2
        if digit_2 < 0:
            print(f'{digit_1} * ({digit_2}) = {result}')
        else:
            print(f'{digit_1} * {digit_2} = {result}')
    elif sign == '/':
        result = digit_1 / digit_2
        if digit_2 < 0:
            print(f'{digit_1} / ({digit_2}) = {result}')
        else:
            print(f'{digit_1} / {digit_2} = {result}')
    else:
        print('Вы ввели неверный знак операции')

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

digit = input('Введите любое натуральное число: ')  # Не делала сразу перевод в int, так как хотела при вводе,
# например, "000" увидеть "3" четных числа
digit_for_print = digit
len_digit = len(str(digit))
even_amount_num = 0
odd_amount_num = 0

while len_digit != 0:
    last_digit = int(digit) % 10
    if last_digit % 2 == 0 or last_digit == 0:
        even_amount_num = even_amount_num + 1
    elif last_digit % 2 != 0:
        odd_amount_num = odd_amount_num + 1
    len_digit = len_digit - 1
    digit = int(digit) // 10

print(f'Четных цифр в числе {digit_for_print} - {even_amount_num}')
print(f'Нечетных цифр числе {digit_for_print} - {odd_amount_num}')

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843.

digit = int(input('Введите число: '))
digit_for_print = digit
opposite_digit = 0

while digit > 0:
    number = digit % 10
    digit = digit // 10
    opposite_digit = opposite_digit * 10
    opposite_digit = opposite_digit + number

print(f'{digit_for_print} наоборот {opposite_digit}')

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
# (n) вводится с клавиатуры.

n = int(input('Введите количество элементов для суммирования: '))
result = 0
cur_elem = 1

while n > 0:
    result = result + cur_elem
    cur_elem = cur_elem * (-1) * 0.5
    n = n - 1

print(result)

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
# заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
# "код-символ" в каждой строке.

a = 32
b = 127

for i in range(a, b + 1):
    print(f'{i} --> {chr(i)}', end=' | ')
    if i % 10 == 0:
        print('')

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, то вывести загаданное число.

from random import randint

random_number = randint(0, 101)
try_amount = 1

while try_amount < 10:
    user_number = int(input('Угадайте число от 0 до 100: '))
    if user_number < random_number:
        print('Введенное число меньше загаданного')
        print(f'У Вас осталось {10 - try_amount} попыток')
    elif user_number > random_number:
        print('Введенно число больше загаданного')
        print(f'У Вас осталось {10 - try_amount} попыток')
    try_amount = try_amount + 1
else:
    print(random_number)


# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите любое натуральное число: '))
result = n * (n + 1)/2
sum_n = 0

for i in range(1, n + 1):
    sum_n += i

if result == sum_n:
    print(True)
else:
    print(False)

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом
# с клавиатуры.

from random import randint

number = int(input('Введите цифру, которую необходимо посчитать: '))
amount_numbers = int(input('Введите количество чисел в последовательности: '))

num_list = [randint(1, 10) for i in range(amount_numbers)]

if number in num_list:
    print(f'Число {number} встречается в последовательности, состоящей из {amount_numbers}, '
          f'элементов {num_list.count(number)} раз')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_digit(digit):
    result_sum = 0
    while digit > 0:
        result_sum += digit % 10
        digit //= 10
    return result_sum


num_list = []
for i in range(int(input('Введите длину последовательности для хранения натуральных чисел: '))):
    num_list.append(int(input('Введите натуральное число: ')))

sum_list = []
for elem in num_list:
    sum_list.append(sum_digit(elem))

dict_num = dict(zip(num_list, sum_list))
print(max(dict_num))
