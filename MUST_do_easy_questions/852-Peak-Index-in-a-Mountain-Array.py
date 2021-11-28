def peakIndexInMountainArrayI(arr):
    """
    Straightforward solution, check the grather number in the array, this will be the top of the mountain.
    Big O:
    Time: O(n), n is the numebr in the array
    Space: O(1), no extra speace is necesary
    """
    top_mountain = float('-INF')
    index = 0
    
    for i in range(len(arr)):
        if arr[i] > top_mountain:
            top_mountain = arr[i]
            index = i
        
    return index
        

def peakIndexInMountainArrayII(arr):
    """
    Binary Search Tree.
    Big O:
    Time : O(log n), n is the lenght of A
    Space: O(1), no extra speace is necesary
    """
    left = 0
    right = len(arr) - 1
    
    while (left < right):
        middle = (left + right) // 2
        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return left


# Test Cases

print(peakIndexInMountainArrayI([0,1,0]))
print(peakIndexInMountainArrayI([0,2,1,0]))
print(peakIndexInMountainArrayI([0,10,5,2]))
print(peakIndexInMountainArrayI([3,4,5,1]))
print(peakIndexInMountainArrayI([24,69,100,99,79,78,67,36,26,19]))