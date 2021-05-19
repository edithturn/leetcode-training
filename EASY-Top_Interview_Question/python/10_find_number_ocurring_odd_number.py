# Find the Number Occurring Odd Number of Times

# i = [2,1,1,1,2,7,7,6] |eve , odd
# o = 1 

# i = [2,1,7,1,6, 1,7,2] |eve , odd
# o = [1,6]

# Iterate the first list
# Inizializar the count in 0, and iterate the list again to compare values
# If the element of the firts iteration is equal to the element of second iteration , increase count in 01

def removingDuplicates(n_list):
	f_list = []
	for i in n_list:
		if i not in f_list:
			f_list.append(i)
	return f_list

def searchOdd(array):
	a_size = len(array)
	n_list = []
	for i in range(a_size):
		count = 0
		for f in range(a_size):
			if array[i] == array[f]:
				count += 1
		if (count % 2 != 0):
			n_list.append(array[i])
	return removingDuplicates(n_list)

# Test
_list = [1,2,7,1, 6, 1,7,2, 2]
print(searchOdd(_list))