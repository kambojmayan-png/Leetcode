class Solution(object):
    def maxArea(self, height):
        l,r = 0,len(height)-1
        max_area = 0
        while l < r:
            h = min(height[l],height[r])
            max_area = max(h*(r-l),max_area)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            
        return max_area