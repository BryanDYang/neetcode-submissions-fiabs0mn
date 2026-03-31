class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix approach
        # where we have prefix
        # compare the prefix sum of the pointer
        # to the last prefix sum - ith index prefix sum
        # if they're equal, return the ith index

        n = len(nums)
        prefixSum = 0
        prefix = [0] * n

        for _ in range(n):
            prefixSum += nums[_]
            prefix[_] = prefixSum

        total = prefix[-1]

        for i in range(n):
            leftSum = prefix[i] - nums[i]
            rightSum = total - prefix[i]
        
            if leftSum == rightSum:
                return i

        return -1 
