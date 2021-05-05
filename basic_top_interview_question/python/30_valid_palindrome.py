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


def isPalindrome(s):
    alphanumeric = re.sub(r'[^A-Za-z0-9]+', '',s).lower()

    reversed_alphanumeric = alphanumeric[::-1]
    return  reversed_alphanumeric == alphanumeric

string =  "A man, a plan, a canal: Panama"
print(isPalindromeII(string))

# Runtime: 32 ms
# Memory Usage: 15.3 MB