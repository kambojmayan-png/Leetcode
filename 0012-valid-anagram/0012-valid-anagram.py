class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for i in s:
            count[i] = 1 + count.get(i,0)
        for i in t:
            if i not in count or count[i] == 0:
                return False
            count[i] -= 1
        return True