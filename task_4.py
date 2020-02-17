list_of_palindroms = []
palindrome = 0
for i in reversed(range(999)):
    for j in reversed(range(999)):
        palindrome = i * j
        if str(palindrome)[:3] == str(palindrome)[:2:-1]:
            list_of_palindroms.append(palindrome)
print(max(list_of_palindroms))
