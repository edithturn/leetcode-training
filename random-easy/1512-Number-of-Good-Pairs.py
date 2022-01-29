def numIdenticalPairs(nums):
    hashMap = {}
    res  = 0
    for i in nums:
        if i in hashMap:
            res += hashMap[i] # res = 3 + 1 = 4
            hashMap[i] += 1   # 1:2
        else:
            hashMap[i] = 1 # 1:1  2:1  3:1 
    return res
    
    
print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))
