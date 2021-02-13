# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

#Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

#Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _len = len(digits) - 1
        for index in range(_len, -1, -1):
            if  digits[index] == 9:
                digits[index] = 0
                if index == 0:
                    digits.insert(0,1)
            else:
                digits[index] += 1
                break
        return digits