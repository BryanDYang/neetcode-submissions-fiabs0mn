class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if len(s) < len(t):
            return ""

        window, tCount = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(tCount)
        
        l = 0 
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if window[c] == tCount.get(c, 0):
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
            
                window[s[l]] -= 1
                if window[s[l]] < tCount.get(s[l], 0):
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
