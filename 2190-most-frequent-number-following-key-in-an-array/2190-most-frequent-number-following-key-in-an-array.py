class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        hashmap = {}
        for i in range(len(nums) - 1):
            target = nums[i + 1]
            if nums[i] == key and target not in hashmap:
                for j in range(i , len(nums) - 1):
                    if nums[j] == key and nums[j + 1] == target:
                        hashmap[target] = hashmap.get(target , 0) + 1

        return max(hashmap , key = lambda k: hashmap[k])
        