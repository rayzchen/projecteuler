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

truncatable = []
checked = set(str(p) for p in primes)
for prime in primes[4:]:
    string = str(prime)
    length = len(string)
    is_truncatable = True

    for i in range(length - 1):
        if string[:length - i - 1] not in checked:
            is_truncatable = False
            break
    if not is_truncatable:
        continue

    p = string
    for i in range(length - 1):
        if string[i + 1:] not in checked:
            is_truncatable = False
            break
    if not is_truncatable:
        continue

    truncatable.append(prime)
    if len(truncatable) == 11:
        break
print(sum(truncatable)) # 748317

