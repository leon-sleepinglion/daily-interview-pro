from itertools import combinations

# brute force
# evaluate every triplet formable from the input
# verify if a^2 + b^2 = c^2 where c = the max in triplet
def findPythagoreanTriplets(nums):
  triplets = combinations(nums, 3)
  for triplet in triplets:
    c = max(triplet)
    sum = 0
    for i in triplet:
      if i != c:
        sum += i**2
    if sum == c**2:
      return True
  return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True