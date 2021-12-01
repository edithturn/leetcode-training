def containsDuplicate(nums):
    """
    Dictionary to add num without repetition, if we find a repetition return True.
    Big(O)
    Time: O(n)
    Space: O(n)
    """
    numdic = dict()
    
    for num in nums:
        if num not in numdic:
            numdic[num] = 1
        else:
            return True
    return False
            

# Test Cases
print(containsDuplicate( [1,2,3,1])) # True
print(containsDuplicate( [1,2,3,4])) # False
print(containsDuplicate( [1,1,1,3,3,4,3,2,4,2])) # True

