lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays = []
day = 1

for i in range(101):
    for month in range(12):
        sundays.append(day == 0)
        month_length = lengths[month]
        if month == 1:
            if i % 4 == 0 and i != 0:
                month_length += 1
        day += month_length
        day %= 7

print(sum(sundays[12:])) # 171

