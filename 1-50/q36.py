palindromes = []
for i in range(1, 1000):
    string = str(i)
    a = int(string + string[::-1])
    b = int(string + string[-2::-1])
    for num in [a, b]:
        binary = bin(num)[2:]
        if binary == binary[::-1]:
            palindromes.append(num)
print(sum(palindromes)) # 872187

