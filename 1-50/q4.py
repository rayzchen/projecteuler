numbers = [a*b for a in range(100, 1000) for b in range(100, 1000) if a >= b]
palindromes = [x for x in numbers if (s := str(x)) == s[::-1]]
print(max(palindromes)) # 906609

