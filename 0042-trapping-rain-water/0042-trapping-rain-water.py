class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return n
        
        left_max = [0]*n
        right_max = [0]*n

        for i in range(1 , n):
            left_max[i] = max(left_max[i-1],height[i-1])

        for j in range(n-2,-1,-1):
            right_max[j] = max(right_max[j+1],height[j+1])

        res = 0
        for k in range(n):
            if min(left_max[k],right_max[k]) - height[k] > 0:
                res += min(left_max[k],right_max[k]) - height[k]
        
        return res