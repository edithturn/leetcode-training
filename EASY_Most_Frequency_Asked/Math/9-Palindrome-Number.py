# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false

# Constraints:
# -231 <= x <= 231 - 1


def isPalindrome(x):
    """
    First Approach: Reverse half of the number and compare with the original number

    Big O
    - Time complexity : O(n)
    - Space complexity: O(1)
    """
    revert = 0
    if  x < 0 or (x%10 == 0 and x != 0):
        return False

    while (x > revert):
        revert = revert*10 + x%10
        x //= 10
        
    if x == revert or x == revert//10:
        return True
    else:
        return False
        
# Test Cases

print(isPalindrome(1221))
print(isPalindrome(12321))
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(-101))
print(isPalindrome(0))