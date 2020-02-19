"""
Найдите сумму цифр в числе 100!
"""

import math


def factorial_my(x):
    if x <= 1:
        return 1
    fact = x * factorial_my(x - 1)
    return fact
print(sum([int(i) for i in str(factorial_my(100))]))

print(sum([int(i) for i in str(math.factorial(100))]))


