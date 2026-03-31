class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()

        return not stack 
            
            