import math

n = 0
while True:
    n += 1
    T = n * (n + 1) // 2
    divisors = 0
    for i in range(1, int(math.sqrt(T))):
        if T % i == 0:
            divisors += 2
    if divisors > 500:
        break
print(T) # 76576500

