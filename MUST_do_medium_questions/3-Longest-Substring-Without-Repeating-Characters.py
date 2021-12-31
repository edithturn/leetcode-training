class Solution:
    """
    Slide Window. Keep tracking the leng of the letters which are not repeting.
    Big O:
    Time: O(n)
    Space: O(1)
    """
    def lengthOfLongestSubstring(s):
        tmpSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in tmpSet:
                tmpSet.remove(s[l])
                l += 1
            tmpSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
    
# Test Cases

print(Solution.lengthOfLongestSubstring("abcabcbb")) #3
print(Solution.lengthOfLongestSubstring("bbbbb"))    #1
print(Solution.lengthOfLongestSubstring("pwwkew"))   #3
