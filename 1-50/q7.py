"""
limit is largest n where n^2 < i
counter is how many odd numbers until the next odd square
(n+2)^2 - n^2 = 4n+4, so 2n+2 odd numbers
120000 selected by checking 120000/ln(120000)

"""

primes = [2]
limit = 1
counter = 0
for i in range(3, 120000, 2):
    if counter == 0:
        limit += 2
        counter = 2 * limit + 2
    counter -= 1

    is_prime = True
    for p in primes:
        if p > limit:
            break
        if i % p == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
        if len(primes) == 10001:
            break
print(primes[10000]) # 104743

