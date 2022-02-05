def isSubsequence(s, t):
    if s == "":
        return True
    left = 0
    right = 0
    count = 0
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
            count += 1
            if count == len(s):
                return True               
        right += 1
    return False

print(isSubsequence("abc", "ahbgdc")) # True
print(isSubsequence("axc", "ahbgdc")) # False