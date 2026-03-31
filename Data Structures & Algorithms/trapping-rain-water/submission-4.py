class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

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

        total = 0
        for _ in range(len(height)):
            total += max(min(maxRight[_], maxLeft[_]) - height[_], 0)

        return total
