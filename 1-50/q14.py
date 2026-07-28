lengths = [0, 1]
for i in range(2, 1000000):
    n = i
    length = 1
    while n >= i:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        length += 1
    lengths.append(length + lengths[n] - 1)
print(lengths.index(max(lengths))) # 837799

