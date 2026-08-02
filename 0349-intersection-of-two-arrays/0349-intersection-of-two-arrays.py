class Solution(object):
    def intersection(self, nums1, nums2):
        common = set()
        if (len(nums1) > len(nums2)):
            for i in nums2:
                if i in nums1:
                    common.add(i)
        else:
            for i in nums1:
                if i in nums2:
                    common.add(i)
        common_list = []
        for i in common:
            common_list.append(i)
        return common_list