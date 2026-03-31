class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # O(n^2) solution for time complexity and O(1) space complexity
        # maxHeight = 0

        # for i in range(len(heights)):

        #     for j in range(i + 1, len(heights)):
        #         maxHeight = max(maxHeight, min(heights[i], heights[j]) * (j - i))
        
        # return maxHeight

        # two pointers
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, curArea)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1
        
        return maxArea
            
            

        