def reverseVowels(s):
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    s = list(s)
    left = 0
    right = len(s) - 1        
    while left < right:
        if s[left] in vowels:
            if s[right] in vowels:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                left += 1
                right -= 1                    
            else:
                right -= 1
        else:
            left += 1
    return "".join(s)
    
print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
