class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # initiate A & B arrays
        A, B = nums1, nums2
        # initiate total len of nums1 & nums2
        total = len(nums1) + len(nums2)
        # initiate half
        half = total // 2

        # ensure A < B
        if len(A) > len(B):
            A, B = B, A

        # initiate l & r pointer for A
        l, r = 0, len(A) - 1
        # while loop
        while True:
            # initiate mid pointer for A
            i = (l + r) // 2
            # initiate mid pointer for B
            j = half - i - 2

            # left = mid and right = mid+1
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # check A & B mid pointers
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # compare
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

