def sortArrayByParityII(nums):
    res = []
    even = 0
    odd  = 1
    
    for num in nums:
        if num%2 == 0:
            res.insert(even, num)
            even += 2
        else:
            res.insert(odd, num)
            odd += 2
    return res
                
                
print(sortArrayByParityII([4,2,5,7]))
print(sortArrayByParityII([2,3]))