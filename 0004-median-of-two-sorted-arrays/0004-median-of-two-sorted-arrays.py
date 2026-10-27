class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x,y = nums1,nums2
        total = len(x) + len(y)
        half = (len(x) + len(y))//2

        if len(y) < len(x):
            x,y = y,x

        l,r = 0,len(x)-1

        while True:
            i = (l + r)//2 #x
            j = half - i - 2#y

            xLeft = x[i] if i >= 0 else float("-infinity")
            xRight = x[i + 1] if i + 1 < len(x) else float("infinity")
            yLeft = y[j] if j >= 0 else float("-infinity")
            yRight = y[j + 1] if j + 1 < len(y) else float("infinity")

            if xLeft <= yRight and yLeft <= xRight:
                if total%2 != 0:
                    return min(xRight , yRight)
                
                return (max(xLeft,yLeft) + min(xRight,yRight))/2.0

            elif xLeft > yRight:
                r = i - 1

            else:
                l = i + 1
