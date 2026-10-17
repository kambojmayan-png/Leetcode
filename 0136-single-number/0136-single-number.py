class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i , 0) + 1

        for i in nums:
            if hashmap[i] == 1:
                return i