class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        normalSum = 0
        individualSum = 0
        for i in nums:
            normalSum += i

        for i in nums:
            while i != 0:
                individualSum += i % 10
                i = i // 10

        return abs(normalSum - individualSum)