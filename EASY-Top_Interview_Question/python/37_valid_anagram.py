def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    str1 = list(s)
    str1.sort()
    str2 = list(t)
    str2.sort()

    i = 0
    while i < len(str1):
        if str1[i] == str2[i]:
            i += 1
        else:
            return False
            
    return True
        


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))