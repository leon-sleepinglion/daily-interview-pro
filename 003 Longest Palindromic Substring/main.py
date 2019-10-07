class Solution: 
    def longestPalindrome(self, s):
        if len(s) == 2:
            return s[0]
        longest = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp) > len(longest):
                    longest = temp
        return longest
                
        
# Test program
s = "a"
print(str(Solution().longestPalindrome(s)))
# racecar