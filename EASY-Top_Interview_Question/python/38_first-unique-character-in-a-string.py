def firstUniqChar(s):
    ddic = {}
    for i in s:
        if i not in ddic:
            ddic[i] = 1
        else:
            ddic[i] += 1
    for i in range(len(s)):
        if ddic[s[i]] == 1:
            return i
    return -1        

s = "leetcode"
print(firstUniqChar(s))

s = "loveleetcode"
print(firstUniqChar(s))

s = "aabb"
print(firstUniqChar(s))