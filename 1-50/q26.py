"""
Long-division until a previously encountered remainder is found

"""

lengths = [0, 0]
for d in range(2, 1000):
    carries = [1]
    length = 0
    while True:
        dividend = carries[-1] * 10
        quotient, remainder = divmod(dividend, d)
        if remainder == 0:
            lengths.append(0)
            break
        if remainder in carries:
            lengths.append(len(carries) - carries.index(remainder))
            break
        carries.append(remainder)
print(lengths.index(max(lengths))) # 983

