"""
Prime sieve taken from q7.py

"""

primes = [2]
limit = 1
counter = 0
for i in range(3, 80000, 2):
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

prime_check = set(primes)
longest_pair = None
longest_length = 0
for a in range(-999, 1000):
    for b in primes:
        if b > 1000:
            break

        for n in range(80):
            sequence = n ** 2 + a * n + b
            if sequence < 0:
                break
            if sequence not in prime_check:
                if n - 1 > longest_length:
                    longest_length = n - 1
                    longest_pair = (a, b)
                break

print(longest_pair[0] * longest_pair[1]) # -59231

