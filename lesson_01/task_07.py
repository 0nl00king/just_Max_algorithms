"""

По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника, составленного из этих отрезков.
Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.

"""

print('Введите длины трех отрезков.')
first = float(input('Длинна отрезка a = '))
second = float(input('Длинна отрезка b = '))
third = float(input('Длинна отрезка c = '))

if first + second <= third or first + third <= second or second + third <= first:
    print(f'Треугольник со сторонами {first:.2f}, {second:.2f}, {third:.2f} существовать не может!')
elif first != second and first != third and second != third:
    print(f'Треугольник со сторонами {first:.2f}, {second:.2f}, {third:.2f} разносторонний!')
elif first == second == third:
    print(f'Треугольник со сторонами {first:.2f}, {second:.2f}, {third:.2f} равносторонний!')
else:
    print(f'Треугольник со сторонами {first:.2f}, {second:.2f}, {third:.2f} равнобедренный!')
