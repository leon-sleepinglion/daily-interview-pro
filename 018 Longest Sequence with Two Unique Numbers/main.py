def findSequence(seq):
  longest_sequence = []
  for i in range(len(seq)):
    for j in range(i+1, len(seq)):
      current_sequence = seq[i:j]
      if len(set(current_sequence)) == 1:
        continue
      elif len(set(current_sequence)) == 2:
        if len(current_sequence) > len(longest_sequence):
          longest_sequence = current_sequence
      else:
        break
  return f'Longest sequence: {longest_sequence}, length: {len(longest_sequence)}'

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4