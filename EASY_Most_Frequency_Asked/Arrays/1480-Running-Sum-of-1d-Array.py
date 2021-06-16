# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSumI(nums):
    """
    First Approach Brute Force: Using Separate Space, create an empty list where I will storage
    the sum of each element iterated in the loop.

    ||======= Big O ======= ||
    - Time complexity : O(n) where n is the length of the input array. We use a single loop that iterates over the entire array to calculate the running sum.
    - Space complexity: O(1)  the output array is not take into consideration
    """
    nlist = []    
    nsum = 0
    for i in range(0, len(nums)):
        nsum = nsum + nums[i]
        nlist.append(nsum)
        
    return nlist


def runningSumII(nums):
    """
    Second Approach Using Input Array for Output: create an empty list where I will storage
    the sum of each element iterated in the loop.

    ||======= Big O ======= ||
    - Time complexity : O(n) where n is the length of the input array. We use a single loop that iterates over the entire array to calculate the running sum.
    - Space complexity: O(1) 
    """
    
    for i in range(1,len(nums)):
       nums[i] = nums[i] + nums[i - 1]

    return nums

# Test Cases
nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]


print("runningSumI")
print(runningSumI(nums1))
print(runningSumI(nums2))
print(runningSumI(nums3))

print("runningSumII")
print(runningSumII(nums1))
print(runningSumII(nums2))
print(runningSumII(nums3))