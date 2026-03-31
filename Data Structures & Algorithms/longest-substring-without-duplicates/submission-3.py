class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initial approach
        # sliding window approach where if we find more than one unique ASCII,
        # move the L pointer until there is no more duplicate 
            # we may have to start at the R in the worst case
        # keep track of the longest substring

        L = 0
        maxSub = 0
        hSet = set()

        for R in range(len(s)):
            while s[R] in hSet:
                hSet.remove(s[L])
                L += 1
            hSet.add(s[R])
            maxSub = max(R - L + 1, maxSub)

        return maxSub
