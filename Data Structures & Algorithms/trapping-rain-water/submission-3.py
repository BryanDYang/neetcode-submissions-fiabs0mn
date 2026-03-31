class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        res = []

        leftMax = 0
        # get max left
        for _ in range(len(height)):
            leftMax = max(leftMax, height[_])
            maxLeft.append(leftMax)

        rightMax = 0
        # get max right
        for _ in range(len(height) - 1, -1, -1):
            rightMax = max(rightMax, height[_])
            maxRight.append(rightMax)
        # reverse the right so indices align with height
        maxRight.reverse()

        for _ in range(len(height)):
            water = min(maxLeft[_], maxRight[_]) - height[_]
            if water > 0:
                res.append(water)           
            else:
                res.append(0)

        return sum(res)
