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

def maxSubArrayI(nums):
    """
    First Approach Brute Force: Two loops, the firs one to have the take the first element in the array and with this start 
    to generate the sum of the sub arrays in the second loop.
    Getting the max sum in a sub array.

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
    - Time complexity : O(n^2) where "n" is the length of nums, wwe have two nested loops, each one is iterating through nums.
    - Space complexity: O(1) I have a list and it will be the result of the substracion of the list
    """
    max_sum_subarray = nums[0]
    current_array = nums[0]
    
    for num in nums[1:]:
       current_array = max(num, current_array + num)
       max_sum_subarray = max(max_sum_subarray, current_array)
    return max_sum_subarray

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
