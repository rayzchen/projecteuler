import math

prod_numerator = 1
prod_denominator = 1

for a in range(1, 10):
    for b in range(1, 10):
        numerator = 10 * a + b
        for c in range(1, 10):
            denominator = 10 * b + c
            if denominator <= numerator:
                continue
            if numerator * c == a * denominator:
                prod_numerator *= numerator
                prod_denominator *= denominator

print(prod_denominator // math.gcd(prod_numerator, prod_denominator)) # 100

