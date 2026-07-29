"""
As proved in q9.py, a+b+c = 2p(p+q) for p>q
840 is the integer below 1000 with the most factors
Therefore a good ansatz = 840

"""

solutions = [0]
for p in range(1, 1001):
    count = 0
    for c in range(p // 2, 3, -1):
        for b in range(c - 1, 2, -1):
            a = p - c - b
            if a >= b:
                break
            if a**2 + b**2 == c**2:
                count += 1
    solutions.append(count)
print(solutions.index(max(solutions))) # 840

