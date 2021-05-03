# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# Example 4:

class Solution:
    def missingNumber(self):
        nums = [0, 3, 2]
        # Lenght of the numbers
        n  = len(nums)
        # Sum of all the numbers from 0 to n
        sumExpected = n*(n + 1 ) // 2
        # Sum the elements of the list 
        sumList = sum(nums)
        # Difference to find the missing number
        return(sumExpected - sumList)

if __name__ == "__main__":
    fb = Solution()
    print (fb.missingNumber())