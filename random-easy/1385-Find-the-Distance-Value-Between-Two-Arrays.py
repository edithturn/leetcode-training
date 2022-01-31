def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for i in arr1:
        for k, v in enumerate(arr2):
            if abs(i - v) <= d:
                break
            if k == len(arr2) - 1:
                count += 1                    
    return count


# Test Cases
print(findTheDistanceValue([4,5,8],[10,9,1,8],2))