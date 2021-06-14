# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

def validPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return is_palindrome(s, i + 1, j) or is_palindrome(s, i, j - 1)
        i += 1
        j -= 1
    return True
    
def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    

# Test Cases
s1 = "aba"
s2 = "abca"
s3 = "abc"
s4 = "beeee"


print(validPalindrome(s1))
print(validPalindrome(s2))
print(validPalindrome(s3))
print(validPalindrome(s4))