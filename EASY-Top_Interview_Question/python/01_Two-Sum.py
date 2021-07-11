class Solution:
    def twoSum_brute_force(self, nums, target):
        """
        Brute Force: Using two loops, two pointers, the second pointer will start in 0 + 1 to start the addition 
        and comparing with the target. The index should be diferent because we can add one number to the same number and compare with the target
        ||======= Big O ======= ||
         * Time complexity : O(n^2)
         * Space complexity: O(1)
        """
        final = []
        
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):       
                if  nums[i] + nums[j] == target and i != j:
                    final.append(i)
                    final.append(j)
                    return final
    def twoSum_hash_table(self, nums, target):
        """
        HashTable: Using a single loop to calculate the complement and check if the complement is in the hastable if it is not I will add tothe hashtable,
        If this is in the hash table, return this number and the index of the num that was par of the complementÑ complement ¿ target ' num
        ||======= Big O ======= ||
         * Time complexity : O(n)
         * Space complexity: O(1)
        """
        fmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in fmap:
                fmap[num] = i
            else:
                return [fmap[complement], i]
# Test Cases
nums1 = [2,5,5,11]
target1 = 10

nums2 = [2,7,11,15]
target2 = 9

sol = Solution()
print(sol.twoSum_brute_force(nums1, target1))
print(sol.twoSum_hash_table(nums2, target2))