def ispalindrome(word):
    return word == word[::-1]
    
def firstPalindrome(words) -> str:
    for word in words:
        result = ispalindrome(word)
        if result:
            return word
    return ""

print(firstPalindrome(["abc","car","ada","racecar","cool"])) # ada
print(firstPalindrome(["notapalindrome","racecar"]))        # racecar
print(firstPalindrome(["def","ghi"]))                       # ""