def reverseWords(s):
    """
    Two pointers: Spliting the string to make a list and iterate. Then swap character of a word afer make it a list (to take each character)
    Bit (O)
    Time: O(n*m)
    Space: O(1)
    """
    words = s.split()
    res = ""
    tmp = []
    
    for word in words:
        l = 0
        r = len(word)-1 
        while l < r:
            word = list(word)
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        res = "".join(word)
        tmp.append(res)
    return ' '.join(tmp)

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))
