"""
d(n) taken from q21.py

"""

import math

def d(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i ** 2 != n:
                total += n // i
    total -= n
    return total

abundant = []
for n in range(1, 28124):
    if d(n) > n:
        abundant.append(n)

is_sum = set()
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        total = abundant[i] + abundant[j]
        if total < 28124:
            is_sum.add(total)
        else:
            break

not_sum = [a for a in range(1, 28124) if a not in is_sum]
print(sum(not_sum)) # 4179871

