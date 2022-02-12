def rotateString(s, goal):
    la, lg = len(s), len(goal)
    
    if la != lg:
        return False
    elif not la and not lg:
        return False
    for i in range(len(s)):
        if s[i] == goal[0] and goal==s[i:] + s[:i]:
            return True
    return False
    
print(rotateString("abcde", "cdeab")) # True
print(rotateString("abcde", "abced")) # False
     
    