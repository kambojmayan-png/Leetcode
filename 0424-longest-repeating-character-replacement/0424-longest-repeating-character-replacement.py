class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,r = 0,0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            if (r - l + 1) - max(count.values()) <= k:
                res = max(res , r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return res