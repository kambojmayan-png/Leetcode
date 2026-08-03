class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0,len(numbers) - 1
        while l < r:
            count = numbers[l] + numbers[r]
            if count == target:
                return l + 1 , r + 1
            elif count < target:
                l += 1
            else:
                r -= 1