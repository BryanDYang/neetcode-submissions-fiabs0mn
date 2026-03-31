class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        # move the left pointer only when there is unique element
        # and assign it to the newly found element from the
        # right pointer
        # at the end of the right pointer loop should finish
        # return the left pointer since there are L amount unique
        # elements

        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1

        return L
            
            