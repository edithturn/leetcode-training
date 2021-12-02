
def smallestEqual(nums):

    """
    Brute Force
    Big O
    Time: O(n)
    Space: O(n)
    """    
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1
    

# Test Cases

print(smallestEqual([0,1,2]))    # 0
print(smallestEqual([4,3,2,1]))  # 2
print(smallestEqual([1,2,3,4,5,6,7,8,9,0])) # -1
print(smallestEqual([2,1,3,5,2])) # 1