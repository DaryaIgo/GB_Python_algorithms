# Урок 5 Коллекции. Список. Очередь. Словарь.

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

db = collections.defaultdict(list)
numbers_firms = 0

while True:
    try:
        numbers_firms = int(input('Введите количество предприятий для анализа: '))
    except ValueError:
        print('Вы ввели не число!')
        continue
    break

count = 0

while count < numbers_firms:
    name_firm = input(f'Введите название предприятия: ')
    profit = [0] * 4
    for i in range(4):
        profit[i] = int(input(f'Введите прибыль {name_firm} за {i + 1}-ый квартал: '))
    print('***')
    db[name_firm] = profit
    count += 1

if count == 1:
    sum_profit = sum(db[name_firm])
    print(f'Предприятие {name_firm}, имеет годовую прибыль {sum_profit}')
elif count > 1:
    avr_firm = {}
    avr_firms_profit = 0

    for firm in db:
        count_1 = 0
        for profit_quarter_firm in db[firm]:
            count_1 += profit_quarter_firm
        avr_firm[firm] = count_1
        avr_firms_profit += count_1

    avr_firms_profit /= len(db)
    print(f'Средняя годовая прибыль для всех предприятий равна {avr_firms_profit}')

low_avr_profit = []
above_avr_profit = []

for firm in avr_firm:
    if avr_firm[firm] > avr_firms_profit:
        above_avr_profit.append(firm)
    else:
        low_avr_profit.append(firm)

if low_avr_profit[0]:
    print(f'Предприятия, которые имеют годовую прибыль НИЖЕ среднего значения: {low_avr_profit}')
if above_avr_profit[0]:
    print(f'Предприятия, которые имеют годовую прибыль ВЫШЕ среднего значения: {above_avr_profit}')
