class Solution(object):
    def mySqrt(self, x):
        i = 0
        res = 0

        while res <= x:
            i += 1
            res = i * i
            
        return i-1