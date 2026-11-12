class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):

            if nums[i] in hashmap:
                if i - hashmap[nums[i]] <= k :
                    return True

            hashmap[nums[i]] = i

        return False