
def twoSum(nums, target):
    values = dict()

    for i, num in enumerate(nums):
        val = target - num
        if val in values:
            return (values[val], i)
        values[num] = i
    return []

list1 = [2,7,11,15]
target1 =  9


list2 = [3, 5, -4, 8, 11, 1, -1, 6]
target2 =10

print(twoSum(list1, target1))
print(twoSum(list2, target2))