def checkString(s):
    
    flag = 0
    
    for i in s:
        if flag == 1:
            if i == 'a':
                return False
        if i == 'b':
            flag = 1
    return True
        
print(checkString("aaabbb")) # True
print(checkString("abab"))  # False