# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

# Example 1:
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
# Example 2:

# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
# Example 3:

# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
 

# Constraints:
# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100


def arraySign1(nums):
    """
    First Approach Brute Force: Iterating the array and product all the values then and if statement to return 0,-1 or 1

    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(1)
    """
    tprod = 1
    
    for i in nums:
        tprod = tprod * (i)
    
    if tprod > 0:
        return 1
    elif tprod < 0:
        return -1
    else:
        return 0
def arraySign2(nums):
    """
    Second Approach Counting negatives

    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(1)
    """
    count = 0

    for i in nums:
        if i == 0:
            return 0
        if i < 0:
            count += 1        
    if count % 2 == 0:
        return 1
    else:
        return -1
        

# Test Cases
nums1 = [-1,-2,-3,-4,3,2,1]
nums2 = [1,5,0,2,-3]
nums3 = [-1,1,-1,1,-1]

print(arraySign1(nums1))
print(arraySign1(nums2))
print(arraySign1(nums3))

print(arraySign2(nums1))
print(arraySign2(nums2))
print(arraySign2(nums3))
