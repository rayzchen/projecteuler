"""
Since n and n+1 are coprime, the number of divisors of
n(n+1)/2 is either d(n/2) * d(n+1) or d(n) * d((n+1)/2)

"""

import math

n = 0
previous_divisors = 1
while True:
    n += 1
    divisors = 0
    if n % 2 == 0:
        to_check = n + 1
    else:
        to_check = (n + 1) // 2

    for i in range(1, int(math.sqrt(to_check)) + 1):
        if to_check % i == 0:
            divisors += 2
            if i ** 2 == to_check:
                divisors -= 1

    if previous_divisors * divisors > 500:
        break
    previous_divisors = divisors
print(n * (n + 1) // 2) # 76576500

