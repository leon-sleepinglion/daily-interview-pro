class MaxStack:
  def __init__(self):
    self.items = []

  # store max so far alongside each value
  def push(self, val):
    if not self.items:
      self.items.append((val, val))
    else:
      self.items.append((val, val if val > self.items[-1][1] else self.items[-1][1]))

  def pop(self):
    self.items.pop()

  def max(self):
    return self.items[-1][1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2