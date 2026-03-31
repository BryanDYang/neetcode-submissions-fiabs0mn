class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_freq = max(max_freq, count[s[r]])

            while (r-l + 1) - max_freq > k:
                count[s[l]] -= 1 
                l += 1
            
            res = max(res, r - l + 1)
            
        return res


        """

        ABABBA  k = 2
        ^
        L
        R
        
        max_freq = 3

        count = {a:1, b:0}

        window = R - L + 1 = 0 - 0 + 1 = 1

        res = 1

        window - max_freq <= k

        5 - 3 = 2 <= k or 2

        """