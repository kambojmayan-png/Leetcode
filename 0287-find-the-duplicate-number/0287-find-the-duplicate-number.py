class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return i
            hashmap[i] = 1