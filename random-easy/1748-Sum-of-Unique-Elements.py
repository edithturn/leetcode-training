def sumOfUnique(nums):
    """
    Using HashMap: Saving the acount of each element, then iterating just the elements in the dic with "1" as a value
    Note: k = number, value = count of appears
    BigO:
    Time:  O(n)
    Space: O(n)
    """
    dicti = {}
    finalSum = 0
    for i in nums:
        if i in dicti.keys():
            dicti[i] += 1
        else:
            dicti[i] = 1
    
    for k, v in dicti.items():
        if v == 1:
            finalSum += k
    return finalSum

# Test Cases    
print(sumOfUnique([1,2,3,2]))           # 4
print(sumOfUnique(nums = [1,1,1,1,1]))  # 0
print(sumOfUnique(nums = [1,2,3,4,5]))  # 15

