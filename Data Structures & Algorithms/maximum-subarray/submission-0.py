class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo: time and space O(n)
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(0, curSum) + num
            maxSum = max(maxSum, curSum)
        
        return maxSum