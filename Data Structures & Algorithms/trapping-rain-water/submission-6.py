class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxL = maxR = total = 0

        L, R = 0, len(height) - 1

        while L < R:
            maxL = max(maxL, height[L])
            maxR = max(maxR, height[R])

            if maxL <= maxR:
                L += 1
                total += max(0, min(maxL, maxR) - height[L])
            else:
                R -= 1
                total += max(0, min(maxL, maxR) - height[R])
        
        return total

            
