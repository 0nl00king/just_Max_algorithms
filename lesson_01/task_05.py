"""

Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

"""

# т.к у нас идеальный пользователь просим его ввести различные буквы иначе бы пришлось добавить if с проверкой
print('Введите две отличающихся буквы английского алфавита в нижнем регистре: ')
first_chr = input('Первая буква : ')
second_chr = input('Втрая буква : ')

ord_first = (ord(first_chr) - ord('a')) + 1
ord_second = (ord(second_chr) - ord('a')) + 1
dif_between = abs(ord_first - ord_second) - 1

print(f'Порядковый номер буквы {first_chr} : {ord_first}')
print(f'Порядковый номер буквы {second_chr} : {ord_second}')
print(f'Между буквами {first_chr} и {second_chr} находится {dif_between} буквы')
