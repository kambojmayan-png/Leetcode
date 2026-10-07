class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc,dec = 0,0
        compare = len(nums) - 1
        for i in range(compare):
            if nums[i] <= nums[i + 1]:
                inc += 1
            if nums[i] >= nums[i + 1]:
                dec += 1

        return inc == compare or dec == compare