class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            string = ""
            for j in range(i,len(s)):
                if s[j] not in string:
                    string += s[j]
                    maxlen = max(maxlen,j-i+1)
                else:
                    break
        return maxlen