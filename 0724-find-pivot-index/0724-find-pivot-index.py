class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - nums[pivot] - left_sum:
                return pivot
            else:
                left_sum += nums[i]
                pivot += 1

        return -1