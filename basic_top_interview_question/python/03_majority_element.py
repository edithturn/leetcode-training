def majorityElement(nums):
	nums = sorted(nums)
	final_number = 0
	final_counter = 0
	counter = 0
	li = len(nums) - 1
	for a in range(li):
		number = nums[a]
		if (number == nums[a + 1]):
			counter = counter + 1
			if counter > final_counter:
				final_counter = counter
				final_number = number
		else:
			counter = 0
	return final_number

li = [2,2,1,1,1,2,2, 4, 4, 4, 4, 4]
print(majorityElement(li))

# Solution
# 1. Sorter the array
# 2. Iterate each element and define final_number and final_counter. 
# 3. Find the first number and set the value in number variable, increment counter in one  while nunber is diferrent than the next one
# 4. If counter > final_counter, final_counter = counter and final_number = number
# 5. return fina_number