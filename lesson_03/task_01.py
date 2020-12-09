"""

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
в том числе написанных самостоятельно.

"""

FROM_NUM = 2
TO_NUM = 100  # 99 + 1
START_DIGIT = 2
END_DIGIT = 10  # 9 + 1

result = [0 for _ in range(END_DIGIT - START_DIGIT)]

for i in range(FROM_NUM, TO_NUM):
    for j in range(START_DIGIT, END_DIGIT):
        if i % j == 0:
            result[j - START_DIGIT] += 1

for idx, num in enumerate(result, start=START_DIGIT):
    print(f'{num} чисел кратно {idx}')
