"""
Prime sieve taken from q7.py

"""

primes = [2]
limit = 1
counter = 0
for i in range(3, 1000000, 2):
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

primes = [str(p) for p in primes]
checker = set(primes)
circular = 0
for p in primes:
    is_circular = True
    for i in range(len(p) - 1):
        p = p[-1] + p[:-1]
        if p not in checker:
            is_circular = False
            break
    if is_circular:
        circular += 1
print(circular) # 55

