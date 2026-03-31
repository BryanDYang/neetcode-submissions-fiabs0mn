class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxA = 0

        while L < R:
            # computer area with current L, R
            minH = min(heights[L], heights[R])
            curA = (R - L) * minH
            maxA = max(curA, maxA)

            # move the pointer at the shorter line
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
            
        return maxA
            