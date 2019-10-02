# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
      l3 = ListNode(0)
      i1, i2, i3 = l1, l2, l3
      while i1 != None:
        i3.val += i1.val + i2.val
        if i3.val >= 10:
            i3.val %= 10
            i3.next = ListNode(1)
        elif i1.next != None:
          i3.next = ListNode(0)
        i1, i2, i3 = i1.next, i2.next, i3.next
      return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val),
  result = result.next
# 7 0 8