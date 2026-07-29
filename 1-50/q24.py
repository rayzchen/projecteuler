"""
We start at 0123456789 which is 1st in lexicographic order
We need to reach 1000000th, passing 999999 numbers
The first digit increases every 9! numbers
The second digit increases every 8! numbers
By subtracting the largest multiple of each factorial, we get
999999 = 9!*2 + 8!*6 + 7!*6 + 6!*2 + 5!*5 + 4!*1 + 3!*2 + 2!*1 + 1!*1 + 0!*0
This means, from the string 0123456789, we take without replacement:
2, 7, 8, 3, 9, 1, 5, 4, 6, 0 = 2783915460

"""

import itertools

last = 0
for i, permutation in zip(range(1000000), itertools.permutations(list(range(10)))):
    if i == 999999:
        last = permutation

print("".join(map(str, last))) # 2783915460

