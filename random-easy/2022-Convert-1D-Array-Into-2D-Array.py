def construct2DArray(original, m, n):
    result = []
    if len(original) == m*n:
        for i in range(0, len(original), n):
            result.append(original[i:i+n])            
    return result
    

print(construct2DArray([1,2,3,4], 2, 2))   # [[1,2],[3,4]]
print(construct2DArray([1,2,3], 1, 3))   # [[1,2,3]]
print(construct2DArray([1,2], 1, 1))     # []