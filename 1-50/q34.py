factorials = [1]
for i in range(10):
    factorials.append(factorials[-1] * (i + 1))

curious = []
for i in range(10, factorials[9] * 7):
    total = 0
    for digit in map(int, str(i)):
        total += factorials[digit]
    if total == i:
        curious.append(total)
print(curious)
print(sum(curious)) # 40730

