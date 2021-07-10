# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment n - 1 elements of the array by 1.

#  Example 1:
# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# Example 2:

# Input: nums = [1,1,1]
# Output: 0 

# Constraints:
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# The answer is guaranteed to fit in a 32-bit integer.


def minMoves(nums):
    """
    First Approach Brute Force: Single pass.

    ||======= Big O ======= ||
    - Time complexity : O(nlog(n)), we have sort function and a while which iterate until the length of the array
    - Space complexity: O(1) , we don't use extra espace
    """
    nums.sort() 
    count = 0
    lenght =  len(nums) - 1
    while lenght >= 0:
        count = count + nums[lenght] - nums[0]
        lenght -= 1
    return count

# Test Cases
nums1 = [1,2,3]
nums2 = [1,1,1]

print(minMoves(nums1))
print(minMoves(nums2))


