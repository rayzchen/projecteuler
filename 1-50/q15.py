"""
Each path can be encoded as a string of 20 Rs and 20 Ds
There are 40!/(20!20!) strings, which is 40C20 = 137846528820

"""

# counts[i][j] is the number of paths from (i, j) to (20, 20)
counts = [[0 for i in range(21)] for i in range(21)]
for i in range(21):
    counts[20][i] = 1
    counts[i][20] = 1
for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        counts[i][j] = counts[i + 1][j] + counts[i][j + 1]
print(counts[0][0]) # 137846528820

