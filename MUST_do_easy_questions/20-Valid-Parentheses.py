def isValid(s):
    """
    Using stack and dictionary. If character is in values store on stack. If char is in keys then compare with the last value on the stack, if they different return false.
    keep comparing with the next element in the stack if they equal pop the value. Is stack empty return 0 return true
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    stack = []
    mydic = {')':'(', ']':'[','}':'{'}
    
    for char in s:
        if char in mydic.values():
            stack.append(char)
        elif char in mydic.keys():
            if stack == [] or mydic[char] != stack.pop():
                return False
        else:
                return False
    return stack == []


# Test Cases

s1 = "()"
print(isValid(s1))

s2 = "()[]{}"
print(isValid(s2))

s3 = "(]"
print(isValid(s3))

s4 = "([)]"
print(isValid(s4))

s5 = "{[]}"
print(isValid(s5))
