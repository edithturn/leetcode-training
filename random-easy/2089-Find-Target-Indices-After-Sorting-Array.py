def targetIndices(nums, target):
    result = []
    
    for i in range(1, target+1):
        count = nums.count(i)
        while count > 0:
            result.append(i)
            count -= 1
    
    final = []
    for i in range(len(result)):
        if result[i] == target:
            final.append(i)
    return final
            
print(targetIndices([1,2,5,2,3], 2)) # [1,2]
print(targetIndices([1,2,5,2,3],3))  # [3]
print(targetIndices([1,2,5,2,3],5))   # [4]