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

truncatable = []
checked = set(primes)
for prime in primes[4:]:
    length = len(prime)
    is_truncatable = True

    for i in range(length - 1):
        if prime[:length - i - 1] not in checked:
            is_truncatable = False
            break
    if not is_truncatable:
        continue

    for i in range(length - 1):
        if prime[i + 1:] not in checked:
            is_truncatable = False
            break
    if not is_truncatable:
        continue

    truncatable.append(int(prime))
    if len(truncatable) == 11:
        break
print(sum(truncatable)) # 748317

