class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurances of val from nums in-place?
        # after removing of all vals, return the number of remaining elements
        # first k elements of numbs do not contain val

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k