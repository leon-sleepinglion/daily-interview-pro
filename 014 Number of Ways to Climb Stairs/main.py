'''
If we look at the solution as a function f(n) where n = number of steps
f(1) = 1
f(2) = 2
f(3) = 3
f(4) = 5
f(5) = 8
f(6) = 13
This is in fact a fibonacci sequence! Hence the solution can be implemented
as a function that calculates the (n+2)th fibonacci number
'''
def staircase(n):
  x = [0,1]
  for i in range(n):
    x.append(x[-1]+x[-2])
  return x[-1]

  
print(staircase(4))
# 5
print(staircase(5))
# 8