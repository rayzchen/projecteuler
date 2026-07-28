"""
Let S be the set of integers in the range [1, 20]
The primes in S are 2, 3, 5, 7, 11, 13, 17 and 19
Let N be the LCM of all elements of S
N has a unique prime decomposition
The power of 2 must be 4 since 16 is in the set
The power of 3 must be 2 since 9 is in the set
The power of 5 and above are all 1
Therefore N = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560

"""

import math
product = 1
for i in range(1, 21):
    product = math.lcm(product, i)
print(product) # 232792560

