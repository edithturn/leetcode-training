# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Examples:

# missing_numbers([1, 3]) #=> [2]
# missing_numbers([2, 3, 7]) #=> [4, 5, 6]
# missing_numbers([-5, -1, 0, 3]) #=> [-4, -3, -2, 1, 2]

def missing_numbers(_list):
    tmp_list = []

    for i in range(_list[0], _list[-1] + 1):
        if i not in _list:
            tmp_list.append(i)
    return tmp_list


list0 = [1, 3]
list1 = [1, 5]
list2 = [2,3,7]
list3 = [-5,-1,0,3]

print(missing_numbers(list0))
print(missing_numbers(list1))
print(missing_numbers(list2))
print(missing_numbers(list3))