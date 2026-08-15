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

        num = 0
        for i in range(len(s) - 1):
            if valueMap[s[i]] < valueMap[s[i + 1]]:
                num -= valueMap[s[i]]
            else:
                num += valueMap[s[i]]
        
        return num + valueMap[s[-1]]