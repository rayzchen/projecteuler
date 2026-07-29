"""
The largest 7-digit number, 9999999, has a power sum of 413343, which is a 6 digit number
Therefore n must be 6 digits long
The largest 6-digit number, 999999, has a power sum of 354294
Therefore n must be at most 354294

"""

powers = [x ** 5 for x in range(10)]
print(powers)

sums = []

for n in range(2, 6 * 9**5):
    digits = n
    total = 0
    while digits:
        digits, final = divmod(digits, 10)
        total += powers[final]
    if n == total:
        sums.append(n)

print(sum(sums)) # 443839

