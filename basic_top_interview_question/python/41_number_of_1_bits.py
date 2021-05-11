class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        count = 0
        i = 0
        while i < 32:
            if n & mask != 0:
                count += 1
            i += 1
            mask <<= 1
        return count
        