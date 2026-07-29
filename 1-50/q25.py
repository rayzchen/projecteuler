"""
Using Binet's formula we see that
F_n = (phi^n + psi^n) / sqrt(5)
where phi = (1+sqrt(5))/2 and psi = (1-sqrt(5))/2
Since |psi| < 1, as n grows large, psi^n tends to 0
We need F_n > 10^999, so log F_n > 999
log F_n can be approximated with n log phi - 0.5 log 5
n log phi - 0.5 log 5 > 999
n log phi > 999 + 0.5 log 5
n > (999 + 0.5 log 5) / log phi
n > 4781.85927
n = 4782

"""

i = 1
a = 1
b = 1
while len(str(a)) < 1000:
    a, b = b, a + b
    i += 1
print(i) # 4782

