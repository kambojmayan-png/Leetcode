class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        for i in range(len(word)):
            word[i] = word[i][::-1]
        
        s = " ".join(word)

        return s