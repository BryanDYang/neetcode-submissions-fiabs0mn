class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        prefixSum = 0
        res = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            if (prefixSum - k) in prefix:
                res += prefix[prefixSum - k]
            prefix[prefixSum] = prefix.get(prefixSum, 0) + 1

        return res