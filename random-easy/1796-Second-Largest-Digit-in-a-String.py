def secondHighest(s):
    """
    Using set to save just numbers.
    Order the set and return the number before the last number
    Big O
    Time :  O(n)
    Space: O(k), where k is len of number in the string
    """
    numbers = set()
    
    for i in s:
        if '0' <= i <= '9':
            numbers.add(i)
    if len(numbers) > 1:
        return sorted(list(numbers))[-2]
    else:
        return -1
    
# Test Cases
print(secondHighest("dfa12321afd"))
print(secondHighest("abc1111"))

