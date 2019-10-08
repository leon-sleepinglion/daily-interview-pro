# naive
# def sortNums(nums):
#   ones = twos = threes = 0

#   for num in nums:
#     if num == 1: ones+=1
#     elif num == 2: twos +=1
#     elif num == 3: threes +=1
  
#   nums[:ones] = [1]*ones
#   nums[ones:ones+twos] = [2]*twos
#   nums[ones+twos:ones+twos+threes] = [3]*threes
  
#   return nums

# O(1) space
def sortNums(nums):
  left = 0
  right = len(nums) - 1
  idx = 0

  while idx < right:
    if nums[idx] == 1:
      nums[left], nums[idx] = nums[idx], nums[left]
      left += 1
      idx += 1
    elif nums[idx] == 2:
      idx += 1
    elif nums[idx] == 3:
      nums[right], nums[idx] = nums[idx], nums[right]
      right -= 1
  
  return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]