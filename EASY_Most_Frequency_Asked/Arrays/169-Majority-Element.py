# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1

import collections

def majorityElement1(nums):
    """
    First Approach Hash Map

    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(n)
    """
    count = collections.Counter(nums)
    return max(count.keys(), key=count.get)

def majorityElement2(nums):
    """
    First Approach Sorting

    ||======= Big O ======= ||
    - Time complexity : O(nlgn)
    - Space complexity: O(1)
    """
    nums.sort()
    return nums[len(nums)//2]

def majorityElement3(nums):
    """
    First Approach  Boyer-Moore Majority Voting Algorithm,  is used to find the majority element
    among the given elements that have more than N/ 2 occurrences.
    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(1)
    """
    mmax = 0
    count = 1
    for i in range(len(nums)):
        if nums[mmax] == nums[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            mmax = i
            count = 1
    return nums[mmax]
        
# Test Cases

nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
nums3 = [2,2,1,1,1,2,2]

print(majorityElement1(nums1))
print(majorityElement2(nums2))
print(majorityElement3(nums3))