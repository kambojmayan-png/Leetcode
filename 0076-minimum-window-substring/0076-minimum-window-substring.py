class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        l = 0
        have = 0
        need_count = len(need)
        res = ""
        minlen = float('inf')

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1 
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            while have == need_count:
                if (r - l + 1) < minlen:
                    res = s[l : r + 1]
                    minlen = r - l + 1

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return res