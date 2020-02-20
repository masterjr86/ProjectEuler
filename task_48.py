"""
Найдите последние десять цифр суммы 1** 1 + 2**2 + 3**3 + ... + 1000**1000.
"""

sum_step = [i**i for i in range(1, 1000)]

lenght = len(str(sum(sum_step)))
print(str(sum(sum_step))[lenght - 10:])