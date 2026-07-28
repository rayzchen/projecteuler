divisible = []
n = 600851475143
for i in range(3, n, 2):
    if n % i == 0:
        while n % i == 0:
            n //= i
        divisible.append(i)
    if n == 1:
        break
print(divisible[-1]) # 6857

