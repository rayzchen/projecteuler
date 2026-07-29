"""
Boolean sieve using only odd numbers
120000 selected by checking 120000/ln(120000)

"""

import math

limit = 120000
sieve = [False] + [True] * (limit // 2 - 1)
maximum = int((math.sqrt(limit) - 1) / 2)
for p in range(1, maximum + 1):
    if sieve[p]:
        for i in range(2 * p * (p + 1), len(sieve), 2 * p + 1):
            sieve[i] = False

count = 1
indexed = 0
for i in range(len(sieve)):
    if sieve[i]:
        count += 1
        if count == 10001:
            indexed = 2 * i + 1
            break
print(indexed) # 104743

