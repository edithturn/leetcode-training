def countPrimes(n):
    """
    Using Sieve of Eratosthenes theoreme, create greather than 10 setting 1 in all of them. Then check all the multiples of a numner less than n are primes and complete them with zero.
    after print the sum of ones which are in the list, they will be the count of primes less then n
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(n)
    """
    if n < 2:
        return 0
    
    s = [1] * n
    s[0] = s[1] = 0
    
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            s[i * i:n:i] = [0] * len(s[i * i:n:i])
    
    return sum(s)

# Test Cases
print(countPrimes(10)) # 4
print(countPrimes(0))  # 0
print(countPrimes(1))  # 0
