
def isHappy(n):
    """
    Two pointer, slow and fast: move the fast pointer until reaches 1 or is equal to slower pointer. If it reaches one return true.
    Squared function to calculate the sum of all the squares of the digits, then move through these number with fast and slow pointers.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    slow = squared(n)
    fast = squared(squared(n))
    while slow != fast and fast != 1:
        slow = squared(slow)
        fast = squared(squared(fast))
        
    return fast==1

def squared(n):
    result = 0
    while n > 0:
        result = result + (n%10)*(n%10)
        n = n//10
    return result

# Test Cases
print(isHappy(20)) # False
#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20

print(isHappy(19)) # True
#19 82 68 100 1

print(isHappy(2)) # False
# 2