class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[n] = i
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash_map and i != hash_map[dif]:
                return [i, hash_map[dif]]