# Referring to: 
# https://web.stanford.edu/class/cs124/lec/med.pdf
# https://www.geeksforgeeks.org/edit-distance-dp-5/
# build a table that calculates the edit distance of the substring
# i.e: from empty string to s2 requires len(s2) costs
# if current char is the same, no cost is added t[i][j] = t[i-1][j-1]
# insert = t[i][j-1], delete = t[i-1][j], substitute = t[i-1][j-1]

def distance(s1, s2):
  m = len(s1) + 1
  n = len(s2) + 1

  table = [[None for y in range(n)] for x in range(m)]

  for i in range(m):
    for j in range(n):
      if i == 0:
        table[i][j] = j
      elif j == 0:
        table[i][j] = i
      elif s1[i-1] == s2[j-1]:
        table[i][j] = table[i-1][j-1]
      else:
        table[i][j] = 1 + min(table[i][j-1], table[i-1][j], table[i-1][j-1])
  
  # print table
  print('  # '+ ' '.join(list(s2)))
  for i in range(m):
    s = s1[i-1] + ' ' if i != 0 else '# '
    for j in range(n):
      s += str(table[i][j]) + ' '
    print(s)

  return table[m-1][n-1]

print(distance('biting', 'sitting'))
# 2