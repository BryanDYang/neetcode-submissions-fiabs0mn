class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        maxLeft = [0] * n
        maxRight = [0] * n

        # build maxLeft in-place
        LeftMax = 0
        for i in range(n):
            LeftMax = max(LeftMax, height[i])
            maxLeft[i] = LeftMax

        # build maxRight in-place
        RightMax = 0
        for i in range(n - 1, -1, -1):
            RightMax = max(RightMax, height[i])
            maxRight[i] = RightMax
        # reverse the right so indices align with height
        # maxRight.reverse()

        total = 0
        for i in range(len(height)):
            total += max(0, min(maxRight[i], maxLeft[i]) - height[i])

        return total
