def missingNumber(nums):
    """
    Addign one number to number in the array until find the missing number
    Big O
    O(n) time
    O(1) space
    """    
    num = 0    
    while num in nums:
        num += 1
    return num
        
# Test Cases
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))