"""
Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""


import math

fact = []

for i in range(1, 10000000):
    if i == sum([math.factorial(int(i)) for i in str(i)]):
        fact.append(i)
print(sum(fact) - 3)
