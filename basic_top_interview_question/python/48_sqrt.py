
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
Force Brute to solve this problem, 2^x = 4 => x = 4^(1/2), then I use int to output the result
"""
def mySqrt(x):
    res = x**(1/2)
    #int_rest = res//1
    return int(res)

n = 4
n1 = 8
# Checking 2^31 - 1 test case
n2 = 2147483648

print(mySqrt(n))
print(mySqrt(n1))
print(mySqrt(n2))