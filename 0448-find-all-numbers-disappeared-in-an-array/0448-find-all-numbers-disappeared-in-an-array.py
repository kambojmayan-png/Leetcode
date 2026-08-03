class Solution(object):
    def findDisappearedNumbers(self, nums):
        num = {}
        for i in range (1 , len(nums) + 1):
            num[i] = 0
        for i in nums:
            num[i] = 1 + num.get(i,0)
        new_list = list()
        for i in range(1 , len(nums) + 1):
            if num.get(i) == 0:
                new_list.append(i)
        return new_list