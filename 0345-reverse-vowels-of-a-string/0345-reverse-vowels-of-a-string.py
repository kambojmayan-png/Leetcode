class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = "AEIOUaeiou"
        s = list(s)

        l,r = 0,len(s) - 1

        while l < r:
            while l < r and s[l] not in vowel:
                l += 1
            while l < r and s[r] not in vowel:
                r -= 1

            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

        return "".join(s)