class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        base = ord('a')
        s1Count = [0] * 26
        s2Count = [0] * 26

        # initial
        for i in range(n):
            s1Count[ord(s1[i]) - base] += 1
            s2Count[ord(s2[i]) - base] += 1
        
        if s1Count == s2Count:
            return True
        
        for r in range(n, m):
            # add the right char
            s2Count[ord(s2[r]) - base] += 1 
            # remove left char
            s2Count[ord(s2[r - n]) - base] -= 1

            if s1Count == s2Count:
                return True
            
        return s1Count == s2Count

