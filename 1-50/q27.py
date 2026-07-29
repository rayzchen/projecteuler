"""
Prime sieve taken from q7.py
80000 selected from estimating 80*1000 to be the limit

"""

import math

limit = 80000
sieve = [False] + [True] * (limit // 2 - 1)
maximum = int((math.sqrt(limit) - 1) / 2)
for p in range(1, maximum + 1):
    if sieve[p]:
        for i in range(2 * p * (p + 1), len(sieve), 2 * p + 1):
            sieve[i] = False

primes = [2] + [2 * i + 1 for i in range(len(sieve)) if sieve[i]]
prime_check = set(primes)
longest_pair = None
longest_length = 0
for a in range(-999, 1000):
    for b in primes:
        if b > 1000:
            break

        for n in range(80):
            sequence = n ** 2 + a * n + b
            if sequence < 0:
                break
            if sequence not in prime_check:
                if n - 1 > longest_length:
                    longest_length = n - 1
                    longest_pair = (a, b)
                break

print(longest_pair[0] * longest_pair[1]) # -59231

