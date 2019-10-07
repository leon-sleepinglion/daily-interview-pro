class Solution:
  def lengthOfLongestSubstring(self, s):
    i = j = 0
    max_length = 1
    seen = set()

    while i < len(s) and j < len(s):
        if s[j] not in seen:
            seen.add(s[j])
            j += 1
        else:
            seen.discard(s[i])
            i += 1
        max_length = max(max_length, j-i)        

    return max_length

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10