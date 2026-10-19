class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        num = 0
        for element in nums:
            if count == 0:
                count += 1
                num = element
            elif num == element:
                count += 1
            else:
                count -= 1

        return num