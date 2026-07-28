"""
Prime sieve taken from q7.py

"""

primes = [2]
limit = 1
counter = 0
for i in range(3, 2000000, 2):
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

print(sum(primes)) # 142913828922

