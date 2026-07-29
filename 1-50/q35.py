"""
Prime sieve taken from q7.py

"""

import math

limit = 1000000
sieve = [False] + [True] * (limit // 2 - 1)
maximum = int((math.sqrt(limit) - 1) / 2)
for p in range(1, maximum + 1):
    if sieve[p]:
        for i in range(2 * p * (p + 1), len(sieve), 2 * p + 1):
            sieve[i] = False

primes = ["2"] + [str(2 * i + 1) for i in range(len(sieve)) if sieve[i]]
checker = set(primes)
circular = 0
for p in primes:
    is_circular = True
    for i in range(len(p) - 1):
        p = p[-1] + p[:-1]
        if p not in checker:
            is_circular = False
            break
    if is_circular:
        circular += 1
print(circular) # 55

