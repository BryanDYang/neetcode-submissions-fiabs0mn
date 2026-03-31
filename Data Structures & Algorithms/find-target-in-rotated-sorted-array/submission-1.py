class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # l to m are sorted
            if nums[l] <= nums[m]:
                # is the target within l to m?
                if nums[l] <= target < nums[m]:
                    # search left
                    r = m - 1
                else:
                    # search right
                    l = m + 1

            # r to m are sorted
            else:
                # is the target within r to m?
                if nums[m] < target <= nums[r]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
        return -1
