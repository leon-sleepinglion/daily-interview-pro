class Solution: 
  def getRange(self, arr, target):
    first = last = -1
    for idx, x in enumerate(arr):
        if x == target:
          if first == -1:
            first = last = idx
          else:
            last = idx
    return [first, last]

  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]