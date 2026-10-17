class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i

        return xor