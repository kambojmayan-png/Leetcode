class Solution(object):
    def reverseString(self, s):
        l,r = 0,len(s)-1
        for i in range(len(s)/2):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s