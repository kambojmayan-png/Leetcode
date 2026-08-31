class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0,len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l + 1 , r + 1]
            elif cur > target:
                r -= 1
            else:
                l += 1
        return []