# Longest Common Prefix

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	prefix = ''
	strs = sorted(strs)
	#print(strs)
	for  i in strs[0]:
		if strs[-1].startswith(prefix+i):
			prefix += i
		else:
			break
	return prefix


# Test
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
