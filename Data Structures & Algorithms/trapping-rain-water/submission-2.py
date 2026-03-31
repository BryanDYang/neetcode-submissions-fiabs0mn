class Solution:
    def trap(self, height: List[int]) -> int:

        # time complexity O(n) & space complexity O(1)
        n = len(height)

        if n == 0:
            return 0
        
        left_max = right_max = 0
        l, r = 0, n - 1
        res = 0

        while l < r:
            if height[l] <= height[r]:
                left_max = max(left_max, height[l])
                res += left_max - height[l] 
                l += 1
            
            else:
                right_max = max(right_max, height[r])
                res += right_max - height[r]
                r -= 1

        return res