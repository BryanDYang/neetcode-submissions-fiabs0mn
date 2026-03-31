class Solution:
    def isPalindrome(self, s: str) -> bool:

        # O(n) solution for tc and sc
        # t = ''.join(c.lower() for c in s if c.isalnum())

        # return t == t[::-1]


        # O(n) tc and O(1) sc
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # helper function
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))