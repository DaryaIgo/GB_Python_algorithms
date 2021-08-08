# Урок 5 Коллекции. Список. Очередь. Словарь.

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import deque

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(x, y):
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            intermediate_result = hex_dict[x.pop()] + hex_dict[y.pop()] + transfer
        else:
            intermediate_result = hex_dict[x.pop()] + transfer
        transfer = 0
        if intermediate_result < 16:
            result.appendleft(hex_dict[intermediate_result])
        else:
            result.appendleft(hex_dict[intermediate_result - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')

    return list(result)


def multi_hex(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_dict[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * hex_dict[x[j]])
        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        intermediate_result = transfer
        for i in range(len(spam)):
            if spam[i]:
                intermediate_result += spam[i].pop()
        if intermediate_result < 16:
            result.appendleft(hex_dict[intermediate_result])
        else:
            result.appendleft(hex_dict[intermediate_result % 16])
            transfer = intermediate_result // 16

    if transfer:
        result.appendleft(hex_dict[transfer])

    return list(result)


num_1 = list(input('Введите 1ое шестнадцатиричное число: ').upper())
num_2 = list(input('Введите 2ое шестнадцатиричное число: ').upper())
print(sum_hex(num_1, num_2))
print(multi_hex(num_1, num_2))
