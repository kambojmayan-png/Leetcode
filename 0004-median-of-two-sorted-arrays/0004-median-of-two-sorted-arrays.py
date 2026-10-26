class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i,j = 0,0

        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
            
        if len(nums)%2 == 0:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2.0

        return nums[len(nums)//2]