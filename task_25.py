"""
Найдите индекс числа Фибоначии, который содержит 1000 цифр
"""


def fib(n):
    fib1 = fib2 = 1
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    yield fib_sum

i = 3
while len(str(next(fib(i)))) < 1001:
    print(len(str(next(fib(i)))), str(next(fib(i))), i)
    i += 1