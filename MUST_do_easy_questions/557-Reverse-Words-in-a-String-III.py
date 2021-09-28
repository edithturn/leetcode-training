def reverseWords(s):
    """
    Using two pointers, right pointer will move until find an space, if space is find it we have a word and we will take it and revert.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(n)
    """
    res = ''
    l,r = 0,0
    
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    # The last word have to complete manually
    res += ' '
    res += s[l:r + 1][::-1]
    return res[1:]
            
# Test Cases
print(reverseWords("Let's take LeetCode contest")) # "s'teL ekat edoCteeL tsetnoc"
print(reverseWords("God Ding")) # "doG gniD"
