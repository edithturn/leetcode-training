# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

def isValid(s):
    """
    First Approach Brute Force, using stack to append the values and remove (pop) if they are not a valid parentheses.
    ||======= Big O ======= ||
    * Time complexity : O(n), becasue we are traversing the given string one character at the time.
    * Space complexity: O(n), we push all the opening brackets onto the stack.
    """
    validator = {')':'(',']':'[','}':'{'}
    stack = []

    for c in s:
        if c in validator.values():
            stack.append(c)
        elif c in validator.keys():
            if stack == []:
                return False
            if validator[c] != stack.pop():
                return False
        else:
            return False
    return stack == []

s1 = "()"
s2 = "()[]{}"
s3 = "(]"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))