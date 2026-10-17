class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        arrSum = 0
        n = len(nums)
        for i in nums:
            arrSum += i

        return (n*(n + 1))//2 - arrSum