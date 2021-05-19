# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

#  Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:

# Input: haystack = "", needle = ""
# Output: 0


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for letter in range(len(haystack) - (len(needle)-1)):
            if haystack[letter : letter + len(needle) ] == needle:
                return letter
        return -1

haystack = "hello"
needle = "ll"

test = Solution()
print(test.strStr(haystack, needle))