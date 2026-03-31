class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxA = 0

        while L < R:
            # compute the area
            minH = min(heights[L], heights[R])
            width = R - L
            curA = width * minH
            maxA = max(curA, maxA)

            # move the shorter line
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return maxA