
"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


"""
01: Force Brute to solve this problem, 2^x = 4 => x = 4^(1/2), then I use int to output the result.
The idea of this exercise is know how sqrt works internatlly, so we sould try to solve in differente way than just using: res = x**(1/2)
"""
def mySqrt1(x):
    res = x**(1/2)
    return int(res)

"""
02: Binary Search Tree.

"""
def mySqrt2(x):
    left = 2
    right = x//2

    if x < 2:
        return x
    while left <= right:
        middle = int(left + (right - left)//2)

        if middle*middle == x:
            return middle           
        elif middle*middle > x:
            right = middle -1
        else:
            left = middle + 1

    return right

n = 4
n1 = 8
# Checking 2^31 - 1 test case
n2 = 2147483647

# Force Brute 
print(mySqrt1(n))
print(mySqrt1(n1))
print(mySqrt1(n2))

# Binary Search Tree.
print(mySqrt2(n))
print(mySqrt2(n1))
print(mySqrt2(n2))