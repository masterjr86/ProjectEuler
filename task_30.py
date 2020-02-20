"""
Найдите сумму всех чисел, которые можно записать как сумму пятых степеней их цифр.
"""

fives = []

for j in range(1000000):
    if j == sum([int(i) ** 5 for i in str(j)]):
        fives.append(j)

print(sum(fives) - 1)