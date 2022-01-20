import math

def canBeIncreasing(nums):
    prev = 0
    flag = False
    nums.append(math.inf)
    i = 0
    _len = len(nums) - 1
    
    while i < _len:
        if prev < nums[i] < nums[i + 1]:
            prev = nums[i]
        else:
            if flag:
                return False
            flag = True
            if nums[i+1] <= prev:
                prev = nums[i]
                i += 1
        i += 1
    return True
            
                
print(canBeIncreasing([1,2,10,5,7])) # True
print(canBeIncreasing([2,3,1,2]))    # False
print(canBeIncreasing([1,1,1]))      # False