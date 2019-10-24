def word_search(matrix, word):
  i = len(matrix)
  j = len(matrix[0])

  # left to right
  for x in range(i):
    if word in ''.join(matrix[x]):
      return True
  
  # up to down
  for x in range(j):
    vector = [matrix[y][x] for y in range(i)]
    if word in ''.join(vector):
      return True
  
  return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True