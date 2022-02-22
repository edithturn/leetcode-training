def diStringMatch( s):
    """
    Two pointers, iterate each character in the string and create a list of number of the size of zero to len(n) + 1
    pointer left will iterate from the left of the list of numbers and pointer right will iterete from the right of the list of numbers
    it is Increasing (start form left) and decreasing(start from right)
    Big O:
    Time: O(n)
    Space:O(1)
    """
    left = 0
    right = len(s)
    res = []
    
    for i in s:
        if i == 'I':
            res.append(left)
            left += 1
        else:
            res.append(right)
            right -= 1

    res.append(left)
            
    return res
                
print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))
