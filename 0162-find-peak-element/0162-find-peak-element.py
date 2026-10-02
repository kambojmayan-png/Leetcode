class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1

        l,r = 1,len(nums) - 2

        while l <= r:
            mid = (l + r)//2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid - 1] > nums[mid]:
                r = mid - 1

            else:
                l = mid + 1