
def rob(nums):
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
print(rob(nums1)) # 4
nums2 = [2,7,9,3,1]
print(rob(nums2)) # 12
nums3 = [2,1,1,2]
print(rob(nums3)) # 4
nums4 = [0]
print(rob(nums4)) # 0
nums5 = [1,2]
print(rob(nums5)) # 2




