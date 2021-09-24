def isAnagram(s, t):
    """
    Using a dictionary to sum each ocurrence of a letter in "s" and substract ocurrence of letter of "t"
    at the end the dictionary should have zero in values.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    dic = {}
    
    if len(s) != len(t):
        return False
    
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    for char in t:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] -= 1
            
    for i in dic.values():
        if i > 0:
            return False
    return True

# Test Cases
print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False