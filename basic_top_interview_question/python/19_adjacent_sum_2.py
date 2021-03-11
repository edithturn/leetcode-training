# Write a method `adjacent_sum` that takes in a list of numbers and returns a new list containing the sums of adjacent numbers in the original list. 
# adjacent_sum([3, 7, 2, 11]) #=> [10, 9, 13], because [ 3+7, 7+2, 2+11 ]
# adjacent_sum([2, 5, 1, 9, 2, 4]) #=> [7, 6, 10, 11, 6], because [2+5, 5+1, 1+9, 9+2, 2+4]


def adjacent_sum(numbers):
    _len = len(numbers) - 1
    _list = []

    for num in range(0, _len):
        val = numbers[num] + numbers[num + 1]
        _list.append(val)
    return _list


list1 = [3,7,2,11]
list2 = [2,5,1,9,2,4]

print(adjacent_sum(list1))
print(adjacent_sum(list2))

# What I learned:
    # Work with index, iterating a specific range of the array
    # Adding to an element the next alement to get a new product
    # Add a new element into a list with append