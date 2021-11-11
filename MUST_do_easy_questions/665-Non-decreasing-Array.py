def checkPossibility(nums):
    """
    Completing values to balance the increasing array. If the current number is less than the previos one, analize the number before previous,
    if this is less or equal than current number, then nivelate the previos number equal to current number, and increase counter in one. 
    If just current number is lower than previos one, cahnge current number with the value of the precious one.
    
    BigO
    -----
    Time: O(n), where n is the lenght of the array.
    Space: O(n), no extra spaces is necesary since we are replacing values
    """
    count = 0
    for i in range(1, len(nums)):
        if(nums[i] < nums[i-1]):
            if(i == 1 or nums[i-2] <= nums[i]):
                nums[i-1] = nums[i]
                count +=1
            else:
                nums[i] = nums[i-1]
                count += 1
    return count <= 1


nums0 = [4,2,3]
nums1 = [4,2,1]
nums2 = [5,7,1,8]
nums3 = [1,4,2]
nums4 = [0,7,1,8]

print(checkPossibility(nums0)) #true
print(checkPossibility(nums1)) #false
print(checkPossibility(nums2)) #true
print(checkPossibility(nums3)) #true
print(checkPossibility(nums4)) #true


