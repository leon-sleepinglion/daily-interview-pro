def check(lst):
  require_mod = False
  for i in range(1, len(lst)):
    if lst[i-1] > lst[i]:
      if not require_mod: require_mod = True
      else: return False
  return True

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False