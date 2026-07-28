numbers = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
numbers += [None] * (1001 - len(numbers))
numbers[20] = "twenty"
numbers[30] = "thirty"
numbers[40] = "forty"
numbers[50] = "fifty"
numbers[60] = "sixty"
numbers[70] = "seventy"
numbers[80] = "eighty"
numbers[90] = "ninety"
numbers[1000] = "onethousand"

for tens in range(2, 10):
    for ones in range(1, 10):
        numbers[10 * tens + ones] = numbers[10 * tens] + numbers[ones]

for hundreds in range(1, 10):
    for tens in range(10):
        for ones in range(10):
            if tens == 0 and ones == 0:
                numbers[100 * hundreds] = numbers[hundreds] + "hundred"
            else:
                numbers[100 * hundreds + 10 * tens + ones] = numbers[100 * hundreds] + "and" + numbers[10 * tens + ones]

print(sum(map(len, numbers))) # 21124

