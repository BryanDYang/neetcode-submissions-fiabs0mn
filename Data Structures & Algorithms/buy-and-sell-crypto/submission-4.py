class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        ans = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            ans = max(ans, prices[R] - prices[L])
        
        return ans