class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,len(s1) - 1
        target = [0]*26
        for i in s1:
            target[ord(i) - ord("a")] += 1

        while r < len(s2):
            count = [0]*26
            for i in range(l,r+1):
                count[ord(s2[i]) - ord("a")] += 1
            if target == count:
                return True
            l += 1
            r += 1
        return False