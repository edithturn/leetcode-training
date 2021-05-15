def isPalindrome(s):
    alphanumeric = ""
    reversed_alphanumeric = ""
    for character in s:
        if character.isalnum():
            alphanumeric += character.lower()
    for c in alphanumeric[::-1]:
        reversed_alphanumeric += c
    return  reversed_alphanumeric == alphanumeric

string =  "A man, a plan, a canal: Panama"
print(isPalindrome(string))

# Runtime: 52 ms
# Memory Usage: 14.7 MB

