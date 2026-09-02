class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j])

        res = 0
        for k in range(n):
            res += min(left_max[k], right_max[k]) - height[k]

        return res
