class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # initiating result and count
        res = count = 0

        # increment the count 1 if num is equal to res other wise -1
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res

"""
This algorithm works because majority element will have n // 2
meaning majority will have at least 1 more than other elements
"""

    