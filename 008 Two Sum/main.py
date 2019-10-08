def two_sum(list, k):
    seen = set()
    for i in list:
        if k - i in seen:
            return True
        seen.add(i)
    return False

print(two_sum([4,7,1,-3,2], 5))