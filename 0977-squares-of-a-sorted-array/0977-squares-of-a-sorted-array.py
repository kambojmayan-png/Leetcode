class Solution(object):
    def sortedSquares(self, nums):
        l, r = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] * nums[l]
                l += 1
            else:
                result[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return result
