class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # dictionary?
        # adding common char comparing one string at a time?
        # O(n * m)

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return res 
            res += strs[0][i]

        return res

