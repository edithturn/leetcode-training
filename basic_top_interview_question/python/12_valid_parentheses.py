# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
	#Open brackets must be closed by the same type of brackets.
	#Open brackets must be closed in the correct order.


def isValid(s: str) -> bool:
	is_valid = True
	stack = []
	open_p = ['(', '{', '[']
	close_p = [')', '}', ']' ]
	for i in s:
		if i in open_p:
			stack.append(i)
		elif i in close_p:
			if len (stack) <= 0:
				return False
			if open_p.index(stack.pop()) != close_p.index(i):
				return False
	return len(stack) == 0

s = "{[]}"
print(isValid(s))