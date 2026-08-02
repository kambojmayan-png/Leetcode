class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        stringS = {}
        stringT = {}
        for i in range(len(s)):
            stringS[s[i]] = 1 + stringS.get(s[i],0)
            stringT[t[i]] = 1 + stringT.get(t[i],0)
        if stringS == stringT:
            return True
        else:
            return False