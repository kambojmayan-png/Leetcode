class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        for key,value in hashmap.items():
            if value != 1:
                return key