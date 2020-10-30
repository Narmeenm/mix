
def twoSum(nums,target):
    i = 0
    check = False
    index = []
    while i < len(nums) and check == False:
        j = i +1
        while j < len(nums) and check == False:
            if nums[i] + nums[j] == target:
                check = True
                second = j
            j +=1
        if check == True:
            index.append(i)
            index.append(second)
        i +=1
    return index
nums = [6,3,5,2]
target = 11

print(twoSum(nums,target))


def sum_two(nums,target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

print(sum_two(nums,target))
