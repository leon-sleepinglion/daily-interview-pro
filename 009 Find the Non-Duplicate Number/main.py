def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums), 2):
        if i == len(nums) -1: return nums[i]
        if nums[i] != nums[i+1]: return nums[i]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1