class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(t) == 0:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        res, window = "", {}
        have, need_count = 0, len(need)
        l, min_len = 0, float('infinity')

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                #update
                if (r - l + 1) < min_len:
                    res = s[l:r+1]
                    min_len = len(res)

                #pop from left
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return res if min_len != float('infinity') else ""