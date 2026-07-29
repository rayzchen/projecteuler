"""
The spiral is formed by a central 1 surrounded by rings
Each ring is an arithmetic progression:
Ring 1: 3, 5, 7, 9 (d=2)
Ring 2: 13, 17, 21, 25 (d=4)
Ring n has d=2n and ends on (2n+1)^2
First element of ring n: (2n+1)^2 - 3 * 2n
Total of ring n: 4 * (2 * (2n+1)^2 - 3 * 2n) / 2
= 4 * (2n+1)^2 - 12n
= 16n^2 + 4n + 4
1001x1001 spiral has 500 rings around a central 1
Sum of first 500 rings:
16 * 500(501)(1001)/6 + 4 * 500(501)/2 + 4(500) + 1 = 669171001

"""

total = 1
current = 1
for i in range(2, 1001, 2):
    for j in range(4):
        current += i
        total += current
print(total) # 669171001

