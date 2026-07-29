"""
Since 918273645 is a pandigital, a larger pandigital must start with 9
Let k be the generating integer of the pandigital. k must start with 9
k cannot be 1 digit long, because that generates 918273645
k cannot be 2 digits long, because 2k, 3k are 3 digits long so the result is 11 digits long
k cannot be 3 digits long, because 2k, 3k are 4 digits long so the result is 10 digits long
k cannot be 5 digits long, because 2k is 6 digits long so the result is 11 digits long
Therefore k is 4 digits long, 2k is 5 digits long

k > 9000 so 2k > 18000
2k cannot contain a 9, so 2k < 19000
Therefore k < 9500
The 2nd digit of k can only be 2, 3, 4
2k cannot start with 198 or 199, so the 2nd digit of k cannot be 4
If the 2nd digit of k is 3, we have 93xx186xx or 93xx187xx

If the 3rd digit is 5 or 6, we have 93xx187xx
Selecting 6 gives 936x1872x, with no valid order for the 4 and 5, or 935x1873x, which has a repeated 3
Selecting 5 gives 935x1870x, which has a 0, or 935x1871x, which has a repeated 1

If the 3rd digit is 2 or 4, we have 93xx186xx
Selecting 4 gives 934x1868x or 934x1869x which both have repeated digits
Selecting 2 gives 932x1864x, with no valid order for the 5 and 7, or 932x1865x
9327 * 2 = 18654, so the largest pandigital = 932718654

"""

pandigitals = []
for i in range(1, 100000):
    string = ""
    for j in range(1, 10):
        string += str(i * j)
        if "0" in string:
            break
        if len(set(string)) != len(string):
            break
        if len(string) > 10:
            break
        if len(string) == 9:
            pandigitals.append(int(string))
print(pandigitals[-1]) # 932718654

