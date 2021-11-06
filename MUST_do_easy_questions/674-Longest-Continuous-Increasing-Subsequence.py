def findLengthOfLCIS(nums):
    """
    If current value is grather than previos, it satisfy the condition and we increase counter in one.
    If not we take the max counter and reset the current counter.
    Big O:
    Time: O(n), where n is the number of element in the array
    Space: O(1), extra space is not using
    """
    current_count = 1
    max_count = 0
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_count += 1
        else:
            max_count = max(current_count, max_count)
            current_count = 1
    return max(current_count, max_count)
        
        
# Test Cases
        
nums1 = [1,3,5,4,7]
nums2 = [2,2,2,2,2]

print(findLengthOfLCIS(nums1)) # 3
print(findLengthOfLCIS(nums2)) # 1