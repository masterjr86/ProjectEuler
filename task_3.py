"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

from math import sqrt

num = 600851475143
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

list_of_prime = []

for i in range(1, num):
    if not num % i and is_prime(i):
        list_of_prime.append(i)
        print(list_of_prime)

print(max(list_of_prime))
