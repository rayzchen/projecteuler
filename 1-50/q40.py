"""
d_1 = 1
After 9 digits, the next integer is the 1st 2-digit number, 10
d_10 = the first digit of 10, or 1
After 9 + 45*2 = 99 digits, the next integer is the 46th 2-digit number, 55
d_100 = the first digit of 55, or 5
After 9 + 90*2 + 270*3 = 999 digits, the next integer is the 271st 3-digit number, 370
d_1000 = the first digit of 370, or 3
After 9 + 90*2 + 900*3 + 1777*4 = 9997 digits, the next integer is the 1778th 4-digit number, 2777
d_10000 = the third digit of 2777, or 7
After 9 + 90*2 + 900*3 + 9000*4 + 12222*5 = 99999 digits, the next integer is the 12223rd 5-digit number, 22222
d_100000 = the first digit of 22222, or 2
After 9 + 90*2 + 900*3 + 9000*4 + 90000*5 + 85185*6 = 999999 digits, the next integer is the 85186th 6-digit number, 185185
d_1000000 = the first digit of 185185, or 1
The product required is 1*1*5*3*7*2*1 = 210

"""

counter = 0
current_limit = 1
product = 1
for i in range(1, 1000000):
    counter += len(str(i))
    if counter >= current_limit:
        extra = counter - current_limit
        product *= int(str(i)[-1 - extra])
        current_limit *= 10
        if counter == 7:
            break
print(product)

