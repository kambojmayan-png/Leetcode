class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        hashmap = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                hashmap[target] = hashmap.get(target , 0) + 1

        return max(hashmap , key = lambda k: hashmap[k])