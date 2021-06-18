# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.


def pivotIndex(nums):
    """
     First Approach: Prefix Sum: We are adding all the numbers to get the total sum of them, then I will keep iterating
     the left side and increasing the sum each iteration to compare with the right side, if this is equal that mean that we found
     the pivot and the we return the index. total_sum - left_sum - nums[i] will give us the right side.
    ||======= Big O ======= ||
    - Time complexity : O(n) 
    - Space complexity: O(1)
    """
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        left_sum += nums[i]

    return -1

# Test Cases
nums1 = [1,7,3,6,5,6]
nums2 = [1,2,3]
nums3 = [2,1,-1]
nums4 = [-1,-1,-1,1,1,1]


print(pivotIndex(nums1))
print(pivotIndex(nums2))
print(pivotIndex(nums3))
print(pivotIndex(nums4))