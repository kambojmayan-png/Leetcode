class Solution:
    def romanToInt(self, s: str) -> int:
        valueMap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        l,r = 0,1
        num = 0
        while r < len(s):
            if valueMap[s[l]] < valueMap[s[r]]:
                num = num - valueMap[s[l]]
            else:
                num = num + valueMap[s[l]]
            l += 1
            r += 1
        return num + valueMap[s[l]]