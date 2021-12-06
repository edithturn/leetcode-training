def numOfStrings(patterns, word):
    """
    
    """
    
    count = 0
    
    for i in patterns:
        if i in word:
            count += 1
    return count
    
# Test Cases

print(numOfStrings(["a","abc","bc","d"],"abc")) # 3
print(numOfStrings(["a","b","c"],"aaaaabbbbb")) # 2
print(numOfStrings(["a","a","a"], "ab"))        # 3