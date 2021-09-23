
def isIsomorphic(s, t):
    """
    Using two dictionaries to storage the key of each letter and as a value the letter in the same index of second list
    Note: A list can't have two element with the same key. In case this happended it will return FALSE.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    sd = {}
    td = {}        
    for i in range(len(s)):
        if s[i] in sd and sd[s[i]] != t[i]:
            return False
        if t[i] in td and td[t[i]] != s[i]:
            return False
        sd[s[i]] = t[i]
        td[t[i]] = s[i]            
    return True

# Test Cases
print(isIsomorphic("egg", "add")) # True
print(isIsomorphic("foo", "bar")) # False
print(isIsomorphic("paper", "title")) # True