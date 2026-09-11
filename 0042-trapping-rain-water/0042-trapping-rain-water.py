class Solution(object):
    def trap(self, height):
        if len(height) == 0:
            return 0

        l,r = 0,len(height)-1
        Max_left = height[l]
        Max_right = height[r]

        res = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if min(Max_left,Max_right) - height[l] > 0:
                    res += min(Max_left,Max_right) - height[l]

                Max_left = max(height[l],Max_left)
            
            else:
                r -= 1
                if min(Max_left,Max_right) - height[r] > 0:
                    res += min(Max_left,Max_right) - height[r]
                
                Max_right= max(height[r],Max_right)

        return res