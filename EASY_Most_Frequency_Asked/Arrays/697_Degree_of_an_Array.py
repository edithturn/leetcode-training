# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

from collections import defaultdict
import collections
def findShortestSubArray(nums):
    """
    Approach: grouping the values, to get the indices with longest lenght, and get the degree.
    [1, 1, 2, 2, 2, 3, 1], grouping the values we shoudl have:
    [1, 1, 2, 2, 2, 3, 1] => { 1: [0, 1, 6], 2: [2, 3, 4], 3: [4] }, degree: 3
    Then we should consider values where the lenght == degree:
    1: [0, 1, 6] => subarray length: (6 - 0) + 1 = 7 
    2: [2, 3, 4] => subarray length: (4 - 2) + 1 = 3 <=  this is the minimum/answer

    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(n)
    """
    mmap = collections.defaultdict(list)
    degree = 0
    min_len = float('inf')

    for index, value in enumerate(nums):
        mmap[value].append(index)
        degree = max(degree, len(mmap[value]))

    for key, indices in mmap.items():
        if degree == len(indices):
            min_len = min(min_len, indices[-1] - indices[0] + 1)

    return min_len


# Test Cases
nums1 = [1,2,2,3,1]
nums2 = [1,2,2,3,1,4,2]
nums3 = [1,2,2,3,1]

print(findShortestSubArray(nums1))
print(findShortestSubArray(nums2))
print(findShortestSubArray(nums3))


