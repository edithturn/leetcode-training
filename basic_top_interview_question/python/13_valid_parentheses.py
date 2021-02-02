# Valid Parenthesese to Paris maybe:)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
	#Open brackets must be closed by the same type of brackets.
	#Open brackets must be closed in the correct order.


def isValid(s: str) -> bool:
	_open = ["(", "{", "["]
	_close = [")", "}", "]"]
	stack = []
	for item in s:
		if item in _open:
			stack.append(item)
		else:
			if len(stack) <= 0:
				return False
			else:
				if _open.index(stack.pop()) != _close.index(item) :
					return False
	return len(stack) == 0

#s = "()"
#s = "()[]{}"
#s = "(]"
#s = "([)]"
#s = "{[]}"
#s = "{"
s = "(("
print(isValid(s))