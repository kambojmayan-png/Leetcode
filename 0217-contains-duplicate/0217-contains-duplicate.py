class Solution(object):
    def containsDuplicate(self, nums):
        hash = set()
        for i in nums:
            if(i in hash):
                return True
            hash.add(i)
        return False