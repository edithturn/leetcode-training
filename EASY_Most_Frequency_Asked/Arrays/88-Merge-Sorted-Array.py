# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].


def merge(nums1, m, nums2, n):

    """
    First Approach: Three pointer

    ||======= Big O ======= ||
    - Time complexity : O(m + n) where "n" is the number of elements in the mums list.
    - Space complexity: O(1) I have a list and it will be the result of the substracion of the list
    """
    p1 = m - 1
    p2 = n - 1
            
    for p in range(m + n  - 1 , -1, -1):
        if p2 < 0:
            break
        if nums1[p1] > nums2[p2] and p1 >= 0:                
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1

# Test Cases

nums1 = [2,0]
n1 = 1
nums2 = [1]
n2 = 1


print(merge(nums1, n1, nums2, n2))