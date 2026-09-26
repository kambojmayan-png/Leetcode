class Solution(object):
    def climbStairs(self, n):
        if n == 1 or n == 2 : return n

        a,b = 1,2
        c = 0

        for i in range(n-2):
            c = a + b
            b,a = c,b

        return c