"""
For a pythagorean triple (a, b, c):
a = p^2 - q^2
b = 2pq
c = p^2 + q^2
where p > q

a+b+c = 2p(p+q)

p(p+q) = 500
If p < 16 then p^2 < 250 so q > p
Therefore p >= 16
If p > 22 then p^2 > 500 so q < 0
Therefore p <= 22

20 * (20 + 5) = 500
Therefore a = 375, b = 200, c = 425
(8-15-17 triangle multiplied by 25)
abc = 8*15*17 * 25^3 = 31875000

"""

triple = None

for c in range(998, 3, -1):
    for b in range(1000 - c - 1, 2, -1):
        a = 1000 - c - b
        if a**2 + b**2 == c**2:
            triple = (a, b, c)
            break
    if triple is not None:
        break
print(triple[0] * triple[1] * triple[2]) # 31875000

