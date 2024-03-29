# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
import math

def maxSubArrayI(nums): # TODO: Time Time Limit Exceeded	
    """
    First Approach Brute Force: Calculate the sucessive sum of a subarray(starting in each point),
    then get the max value of the current sum and the new max sum of a sub array.
    ||======= Big O ======= ||
    - Time complexity : O(n^2) where "n" is the length of nums, wwe have two nested loops, each one is iterating through nums.
    - Space complexity: O(1) I have a list and it will be the result of the substracion of the list
    """
    max_sum_subarray = -math.inf
    
    for i in range(len(nums)):
        current = 0
        for j in range(i, len(nums)):
            current = current + nums[j]
            max_sum_subarray = max(max_sum_subarray, current)
    return max_sum_subarray


"""
Note: Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a possibility. 
"""
def maxSubArrayII(nums):
    """
    Second Approach Dinamic Programming
    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(1) 
    """
    max_sum_subarray = nums[0]
    current_array = nums[0]
    
    for num in nums[1:]:
       current_array = max(num, current_array + num)
       max_sum_subarray = max(max_sum_subarray, current_array)
    return max_sum_subarray


def maxSubArrayIII(nums): # TODO: Time Time Limit Exceeded	
    """
    First Approach Divide and Conquer: 

    ||======= Big O ======= ||
    - Time complexity : 
    - Space complexity:
    """
    def findBestSubarray(nums, left, right):
        current = 0            
        max_left_size = 0
        max_right_size = 0
        mid = (left +  right)//2
        
        if left > right:
            return -math.inf


        for i in range(mid - 1, left - 1, -1):
            current = current + nums[i]
            max_left_size = max(current, max_left_size)

        current = 0
        for j in range(mid + 1, right + 1):
            current = current + nums[j]
            max_right_size = max(current, max_right_size)

        maximum_subarray = nums[mid] + max_left_size + max_right_size
        left_half = findBestSubarray(nums, left, mid - 1)
        right_half = findBestSubarray(nums, mid + 1 , right)
        
        return max(maximum_subarray, left_half, right_half)
    
    return findBestSubarray(nums, 0, len(nums) - 1)

# Test Cases

nums1 = [1]
nums2 = [-2,1,-3,4,-1,2,1,-5,4]
nums3 = [5,4,-1,7,8]


print(maxSubArrayI(nums1))
print(maxSubArrayI(nums2))
print(maxSubArrayI(nums3))


print(maxSubArrayII(nums1))
print(maxSubArrayII(nums2))
print(maxSubArrayII(nums3))


print(maxSubArrayIII(nums1))
print(maxSubArrayIII(nums2))
print(maxSubArrayIII(nums3))
