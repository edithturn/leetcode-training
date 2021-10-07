
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
2

"""
2  2*2 = 4
4  4*4 = 16
16 1*1 + 6*6 = 37
37 3*3 + 7*7 = 58
58 5*5 + 8*8 = 89
89 8*8 + 9*9 = 145
145 1*1 + 4*4 + 5*5 = 42
42 4*4 + 2*2 = 20
20 2*2 + 0+0 = 4 
"""

def isHappyII(n):
    """
    Time: O(log(n))
    Space: O(log(n))n is the number of didits.
    """
    element_in_set = set()
    while(n > 1 and n not in element_in_set):
        element_in_set.add(n)
        n = helper(n)    
    #return n == 1

    if n == 1:
        return True
    elif(n != 1):
        return False

def helper(n):
    sum = 0
    while(n > 0):
        sum += (n % 10)*(n % 10)
        n = n//10
    return sum



# Test Cases
print(isHappyII(20)) # False
#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
print(isHappyII(19)) # True
#19 82 68 100 1
print(isHappyII(2)) # False
print(isHappyII(7)) # True
