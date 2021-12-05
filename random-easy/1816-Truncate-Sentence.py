
def truncateSentence(s, k):
    """
    Keep tracking the number of words visited
    Big(O):
    Time: O(n)
    Space: O(n)
    """
    count = 0
    
    for i in range(len(s)):
        if s[i] == " ":
            count += 1
            if count == k:
                return s[0: i]
        if i == len(s) - 1:
            count = i + 1
    return s[0: count]
            
# Test Cases
print(truncateSentence("Hello how are you Contestant", 4)) # "Hello how are you"
print(truncateSentence("What is the solution to this problem", 4)) #  "What is the solution"
print(truncateSentence("chopper is not a tanuki", 5)) # "chopper is not a tanuki"