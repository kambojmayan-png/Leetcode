class Solution(object):
    def trap(self, height):

        if not height: return 0

        l,r = 0,len(height)-1
        Max_left = height[l]
        Max_right = height[r]

        res = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                Max_left = max(height[l],Max_left)
                res += Max_left - height[l]
  
            else:
                r -= 1
                Max_right= max(height[r],Max_right)
                res += Max_right - height[r]
                
        return res