class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}

        for i, val in enumerate(nums):
            if nums[i] in hmap and abs(i - hmap[val]) <= k:
                return True
            hmap[val] = i
            
        return False
