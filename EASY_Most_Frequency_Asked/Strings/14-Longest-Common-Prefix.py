# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    shortest = min(strs, key=len)    
    
    for index, value in enumerate(shortest):
        for word in strs:
            if word[index] != value:
                return shortest[:index]
    return shortest



str1 = ["flower","flow","flight"]
str2 = ["dog","dogracecar","dogcar"]

print(longestCommonPrefix(str1))
print(longestCommonPrefix(str2))