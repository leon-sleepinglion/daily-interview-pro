class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  if root_node.value == k:
    return (k,k)

  if k < root_node.value:
    next = root_node.left
    ceil = root_node.value
  else:
    next = root_node.right
    floor = root_node.value

  if not next:
    if not floor or not ceil:
      return None
    else:
      return (floor, ceil)

  if k > next.value:
    if not floor:
      return findCeilingFloor(next, k, next.value, ceil)
    elif k - floor > k - next.value:
      return findCeilingFloor(next, k, next.value, ceil)
    else:
      return findCeilingFloor(next, k, floor, ceil)
  
  elif k < next.value:
    if not ceil:
      return findCeilingFloor(next, k, floor, next.value)
    elif ceil - k > next.value - k:
      return findCeilingFloor(next, k, floor, next.value)
    else:
      return findCeilingFloor(next, k, floor, ceil)

  else:
    return (k,k)

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)