digits = set("123456789")
pandigitals = set()

for a in range(2, 100):
    for b in range(100, 100000):
        c = a * b
        candidate = str(a) + str(b) + str(c)
        if len(candidate) > 9:
            break
        if set(candidate) == set(digits):
            pandigitals.add(c)

print(sum(pandigitals)) # 45228

