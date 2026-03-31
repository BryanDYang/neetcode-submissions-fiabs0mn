class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # base cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        cache = [-1] * len(nums)
        
        def dfs(i):
            if i >= n:
                return 0

            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return cache[i]
        
        return dfs(0)