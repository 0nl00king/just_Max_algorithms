"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
 (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
 и вывести наименования предприятий, чья прибыль выше среднего
 и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

# задаем константы:
START_FROM = 1
QUARTER = 3

Company = namedtuple('Company', ['company_name', 'fiscal_year', 'quarter_profit'])
entrprises = set()  # чтобы исключить дубли

company_total_num = int(input('Введите число предприятий для формирования отчета:\n'))
total_profit = 0
for i in range(START_FROM, company_total_num + 1):
    quarter_profit = 0
    fiscal_year = []
    company_name = input('Название {i}-го предприятия:\n')

    for j in range(QUARTER + 1):
        fiscal_year.append(int(input(f'Какова прибыль за {j + 1} квартал ?\n')))
        quarter_profit += fiscal_year[j]

    company = Company(company_name=company_name, fiscal_year=tuple(fiscal_year), quarter_profit=quarter_profit)

    entrprises.add(company)
    total_profit += quarter_profit

average_anual_profit = total_profit / company_total_num

print(f'Отчет по прибыли:\nСреднегодовая прибыль :\n{average_anual_profit}')
for company in entrprises:
    if company.quarter_profit > average_anual_profit:
        print(f'Прибыль выше среднего :\n{company.company_name} : {company.quarter_profit}')
    elif company.quarter_profit < average_anual_profit:
        print(f'Прибыль ниже среднего :\n{company.company_name} : {company.quarter_profit}')
    else:
        print(f'Прибыль равна среднегодовой :\n{company.company_name} : {company.quarter_profit}')
