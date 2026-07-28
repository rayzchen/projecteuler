"""
Sum of all multiples of 3 below 1000:
S1 = (3 + 999) * 333 / 2
Sum of all multiples of 5 below 1000:
S2 = (5 + 995) * 199 / 2
Sum of all multiples of 15 below 1000:
S3 = (15 + 990) * 66 / 2

Desired total: S1 + S2 - S3 = 233168

"""

multiples = set()
for i in range(0, 1000, 3):
    multiples.add(i)
for i in range(0, 1000, 5):
    multiples.add(i)
print(sum(multiples)) # 233168

