class Solution:
    def maxArea(self, heights: List[int]) -> int:
        minH = maxA = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                minH = min(heights[i], heights[j])
                maxA = max(maxA, minH * (j - i))
        
        return maxA