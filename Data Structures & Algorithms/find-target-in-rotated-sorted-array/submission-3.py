class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # mid is in left sorted portion of the array
            if nums[l] <= nums[m]:
                # if the target is within left array, we want to stay in the left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: # target > nums[m]
                # we'll search the rigth side
                    l = m + 1
            # mid is in right sorted portion of the array
            else:
                # if the target is within right array, we want to stay in the right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
