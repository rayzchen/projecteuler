"""
If a^b = c^d and a < c, then c must be a rational power of a
The possible a that produce non-unique terms are:
2^k: 4, 8, 16, 32, 64
3^k: 9, 27, 81
4^k: 16, 64, (8), (32)
5^k: 25
6^k: 36
7^k: 49
8^k: 64, (16), (32)
9^k: 81, (27)
10^k: 100
16^k: (32), (64)
32^k: (64)
27^k: (81)

Integer overlaps (c is an integer power of a):
a=4, 9, 16, 25, 36, 49, 64, 81, 100 will produce existing terms when b <= 50
This will produce 9*49 duplicates
a=8, 27 will produce existing terms when b <= 33
This will produce 2*32 duplicates
a=32 will produce existing terms when b <= 20
This will produce 19 duplicates

Non-integer overlaps (c is a non-integer power of a):
a=8 will produce existing terms when 33 < b <= 66 and b is even (8^2k = 2^6k = 4^3k)
This will produce 17 new duplicates
a=32 will produce existing terms when 20 < b <= 40 and b is divisible by 2 (32^2k = 2^10k = 4^5k)
This will produce 10 new duplicates
a=16 will produce existing terms when 50 < b <= 75 and b is divisible by 3 (16^3k = 2^12k = 8^4k)
This will produce 9 new duplicates
a=32 will produce existing terms when 20 < b <= 60 and b is divisible by 3 (32^3k = 2^15k = 8^5k)
This will produce 11 new duplicates (excludes 24, 30, 36)
a=27 will produce existing terms when 33 < b <= 66 and b is even (27^2k = 3^6k = 9^3k)
This will produce 17 new duplicates
a=32 will produce existing terms when 20 < b <= 80 and b is divisible by 4 (32^4k = 2^20k = 16^5k)
This will produce 8 new duplicates (excludes 24, 28, 32, 36, 40, 48, 60)
a=64 will produce existing terms when 50 < b <= 66 and b is even (64^2k = 2^12k = 16^3k)
This will produce 8 new duplicates
a=64 will produce existing terms when 50 < b <= 80 and b is divisible by 5 (64^5k = 2^30k = 32^6k)
This will produce 5 new duplicates (excludes 60)
a=81 will produce existing terms when 50 < b <= 75 and b is divisible by 3 (81^3k = 3^12k = 27^4k)
This will produce 9 new duplicates

Remaining unique terms: 99^2 - 9*49 - 2*32 - 19 - 17 - 10 - 9 - 11 - 17 - 8 - 8 - 5 - 9 = 9183

"""

terms = set()
for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a ** b)
print(len(terms)) # 9183

