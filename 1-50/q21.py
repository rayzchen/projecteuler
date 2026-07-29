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

amicable = []
for a in range(1, 10000):
    if a in amicable:
        continue
    b = d(a)
    a1 = d(b)
    if a == a1 and a != b:
        amicable.append(a)
        amicable.append(b)

print(sum(amicable)) # 31626

