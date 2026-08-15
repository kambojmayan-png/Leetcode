class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        l, r = 0, k

        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        while r < len(nums):
            window_sum = window_sum - nums[l] + nums[r]
            max_sum = max(max_sum, window_sum)

            l += 1
            r += 1

        return max_sum / k