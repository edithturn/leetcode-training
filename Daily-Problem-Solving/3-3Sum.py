
def threeSum(nums):
    """
    Two pointers, left and right will keep moving if sum is not equal to complement. If sum is less than complement move left pointer, if sum is grather than complemnt
    move right pointer.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    # Order the elements in the array
    nums = sorted(nums)
    # Set to avoid duplicates
    result = set()
    # Iterate until reach the last element in the array
    for i in range(len(nums)):
        # left pointer inicialize index in i + 1
        l = i + 1
        # Right pointer inicialize index in the last elemnt in the array
        r = len(nums) - 1
        # Similar to 2Sum,calculate the complement: target - current number
        complement = 0 - nums[i]
        # Find the two numbers which added each other will give complemt
        while(l < r):
            # It the sum of both number are equal to complement, add the list in result list
            if(nums[l] + nums[r] == complement):
                result.add((nums[i],nums[l],nums[r]))
                # move the left and right pointer
                l += 1
                r -= 1
            # If the sum of both number are less than complement, just move left pointer -> list are in order, so l += 1 we will take a grather number to match complement
            elif(nums[l] + nums[r] < complement):
                l += 1;
            else:
                r -= 1;
    return list(result)
        

# Tests Cases
print(threeSum([-1,0,1,2,-1,-4])) # output [[-1,-1,2],[-1,0,1]]
print(threeSum([])) # output []
print(threeSum([0])) # output: []