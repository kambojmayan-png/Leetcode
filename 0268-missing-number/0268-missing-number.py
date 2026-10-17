class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1

        for i in range(len(nums) + 1):
            if i not in hashmap:
                return i