class Solution:
  def isValid(self, s):
    stack = []
    opening_bracket = ['(', '[', '{']

    for char in s:
        if char in opening_bracket:
            stack.append(char)
        elif char == ')' and stack.pop() != '(':
            return False
        elif char == ']' and stack.pop() != '[':
            return False
        elif char == '}' and stack.pop() != '{':
            return False
    
    return True if not stack else False
        


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))