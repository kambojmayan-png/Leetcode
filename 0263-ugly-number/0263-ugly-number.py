class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while n%i == 0:
                n /= i
                
        return n == 1