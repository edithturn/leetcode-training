def isSameAfterReversals(num):
    reverted = reverse(num)
    return num == reverse(reverted)
    
def reverse(num):
    c = 0
    while num > 0:
        c = c * 10 + num % 10
        num //= 10
    return c
    
print(isSameAfterReversals(526)) # True
print(isSameAfterReversals(1800)) # False