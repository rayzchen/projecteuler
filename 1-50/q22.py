import os
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "q22_names.txt")
with open(filename) as f:
    names = f.read().rstrip()[1:-1].split("\",\"")

names.sort()
scores = [sum(map(lambda c: ord(c) - 64, name)) for name in names]
adjusted = [scores[i] * (i + 1) for i in range(len(scores))]
print(sum(adjusted)) # 871198282

