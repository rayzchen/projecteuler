"""
Copied from q18.py

"""

import os
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "q67_triangle.txt")
with open(filename) as f:
    text = f.read().rstrip()

triangle = []
for line in text.split("\n"):
    triangle.append([int(x) for x in line.split(" ")])

while len(triangle) > 1:
    bottom = triangle.pop()
    for i in range(len(triangle[-1])):
        triangle[-1][i] += max([bottom[i], bottom[i + 1]])
print(triangle[0][0]) # 7273

