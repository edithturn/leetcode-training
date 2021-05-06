def formatting(llist):
    new_list = ""
    if llist[0] == llist[1]:
        new_list += str(llist[0])
    else:
        new_list = str(llist[0])  +"->" +  str(llist[1])
    return new_list

def findMissingRanges(nums, lower, upper):
    new_list = []
    
    prev = lower - 1
    for i in range(0,len(nums) + 1):
        if i < len(nums):
            curr = nums[i]
        else:
            curr = upper + 1
        if prev + 1 <= curr - 1:
            new_list.append(formatting([prev +1, curr - 1]))
        prev = curr
    return new_list

# [0,1,3,50,75]

nums = [0,1,3,50,75]
lower = 0
upper = 99

print(findMissingRanges(nums,lower, upper))
