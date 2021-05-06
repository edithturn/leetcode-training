def isPowerOfThreeI(n):
    p = 1
    while p != n:
        p *= 3
        if p == n:
            return True
            break
        else:
            if p > n:
                return False
                break
    return True


def isPowerOfThreeII(n):
    p = 1
    while n > 1 and n%3 == 0:
        n /= 3
    if n == 1:
        return True
    return False

n = 27
print(isPowerOfThreeI(n))


n = 45
print(isPowerOfThreeII(n))
            
