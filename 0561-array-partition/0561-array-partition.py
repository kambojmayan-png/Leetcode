class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Msum = 0
        for i in range(0,len(nums),2):
            Msum += nums[i]

        return Msum