# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):
    """
    First Approach Brute Force: Create an empty list where I will storage
    the sum of each element iterated in the loop.

    ||======= Big O ======= ||
    * Time complexity : O(n) 
    * Space complexity: O(n)
    where "n" is the number of elements in the sum list.
    """
    nlist = []    
    nsum = 0
    for i in range(0, len(nums)):
        nsum = nsum + nums[i]
        nlist.append(nsum)
        
    return nlist