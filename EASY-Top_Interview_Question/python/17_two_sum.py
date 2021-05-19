
def twoSum(nums, target):
    values = dict()

    for i, num in enumerate(nums):
        val = target - num

        if val in values:
            print(values[val])
            return (values[val], i)
        values[num] = i

list_ = [2,7,11,15]
target_ =  9

print(twoSum(list_, target_))