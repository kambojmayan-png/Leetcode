class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = []
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vowel.append(i)
            
        l,r = 0,len(vowel)-1

        word = []
        for i in s:
            word.append(i)

        while l < r:
            word[vowel[l]],word[vowel[r]] = word[vowel[r]],word[vowel[l]]
            l += 1
            r -= 1

        return ''.join(word)