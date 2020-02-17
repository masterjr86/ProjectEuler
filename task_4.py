"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


list_of_palindroms = []
palindrome = 0
for i in reversed(range(999)):
    for j in reversed(range(999)):
        palindrome = i * j
        if str(palindrome)[:3] == str(palindrome)[:2:-1]:
            list_of_palindroms.append(palindrome)
print(max(list_of_palindroms))
