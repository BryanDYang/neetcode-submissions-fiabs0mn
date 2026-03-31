class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            L = count = 0
            for R in range(len(s)):
                if s[R] == c:
                    count += 1
                
                while (R - L + 1) - count > k:
                    if s[L] == c:
                        count -= 1
                    L += 1
                
                res = max(res, R - L + 1)
        
        return res