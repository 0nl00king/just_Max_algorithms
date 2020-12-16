import cProfile

#  вариант 1 эратосфен:

inp_num = int(input(f'Введите номер i-го по счёту простого числа, для нахождения.\n'))
n = inp_num * 50
array = [i for i in range(n)]
array[1] = 0

for i in range(2, n):
    if array[i] != 0:
        j = i + i
        while j < n:
            array[j] = 0
            j += i

for i in array:
    if i != 0:
        inp_num -= 1
        if inp_num == 0:
            print(f'i-е по счёту простое число: {i}')


#  вариант 2 не эратосфен:

def sieve_01(num):
    count = 1
    prime = 2

    while count < num:
        prime += 1
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                break
        else:
            count += 1
    return prime


inp_num = int(input(f'Введите номер i-го по счёту простого числа, для нахождения.\n'))
print(f'i-е по счёту простое число: {sieve_01(inp_num)}')

cProfile.run('sieve_01(100_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  1    0.000    0.000   10.614   10.614 <string>:1(<module>)
#  1   10.614   10.614   10.614   10.614 task_02.py:25(sieve_01)
#  1    0.000    0.000   10.614   10.614 {built-in method builtins.exec}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
