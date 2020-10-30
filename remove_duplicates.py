sorted_nums = [0,0,1,1,2,3,3,4,5,5]

i = 0
while i < len(sorted_nums):
    if i+1 != len(sorted_nums):
        if sorted_nums[i] == sorted_nums[i+1]:
            sorted_nums.pop(i+1)
        else:
            i +=1
    else:
        i += 1


print(sorted_nums)
