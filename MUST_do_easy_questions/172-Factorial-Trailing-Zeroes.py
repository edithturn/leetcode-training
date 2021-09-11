class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Using two pointers: 10 is the product of 2 and 5. In n! Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
        ||======= Big O ======= || 
        Time complexity : O(log(n))
        Space complexity: O(1)
        """
        i = 5
        count = 0
        
        while n//i >= 1:
            count += n//i
            i *= 5
           
        return count