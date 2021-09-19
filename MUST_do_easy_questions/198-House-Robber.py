
def rob(nums):
    """
    Dinamic Programming: get the sum of nonadjacent values, storage the maximum value in the new list. Each time it will be the max. 
    At the end the max value of nonadjacent value will be at the end of the array
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(n)
    """
    lenght = len(nums)
    
    if lenght == 0:
        return 0
    if lenght == 1:
        return nums[0]
    if lenght == 2:
        return max(nums)

    dp = [0]*lenght
    dp[0], dp[1]= nums[0], max(nums[0], nums[1])
    
    for i in range(2, lenght):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]

# Test Cases
nums1 = [1,2,3,1]
nums2 = [2,7,9,3,1]
nums3 = [2,1,1,2]
nums4 = [0]
nums5 = [1,2]


print(rob(nums1))
print(rob(nums2))
print(rob(nums3))
print(rob(nums4))
print(rob(nums5))

