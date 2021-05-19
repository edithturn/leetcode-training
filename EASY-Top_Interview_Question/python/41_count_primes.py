def countPrimes(n):
    if n <= 2:
        return 0

    primes = [True] * (n)
    count = 0
    num = 2
    while num * num < n:
        if primes[num]:
            multiplier = 2
            while (num * multiplier) < n:
                primes[num * multiplier] = False
                multiplier += 1
        num += 1
    
    for i in range(2, len(primes)):
        if primes[i]:
            count += 1
    return count

n = 10
print(countPrimes(n))