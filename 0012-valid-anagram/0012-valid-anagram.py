class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = 1 + count.get(ch, 0)
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1 
        return True
