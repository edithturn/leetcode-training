def removeDuplicates(nums):
	len_ = 1
	for i in range(1, len(nums)):
		if nums[i] != nums[i - 1]:
			nums[len_] = nums[i]
			len_ += 1
	return (len_)

list_ = [1, 1, 2]
print (removeDuplicates(list_))