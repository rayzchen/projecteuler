"""
Sum of squares is 100*101*201/6
Square of sum is (100*101/2)^2
Square of sum is larger than sum of squares
(a_i)^2 = a_i^2 + 2a_ia_j
(100*101/2)^2 - 100*101*201/6 = 25164150

"""

sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares += i ** 2
square_of_sum = sum(range(1, 101)) ** 2
print(square_of_sum - sum_of_squares) # 25164150

