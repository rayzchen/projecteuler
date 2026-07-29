sizes = [1, 2, 5, 10, 20, 50, 100, 200]

def count(target, largest):
    if target == 0 or largest == 0:
        return 1

    total = 0
    value = 0
    while value <= target:
        total += count(target - value, largest - 1)
        value += sizes[largest]
    return total

print(count(200, 7)) # 73682

