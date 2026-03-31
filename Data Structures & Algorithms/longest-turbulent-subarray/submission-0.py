class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1

        L = 0
        maxLen = 1 # at least one element

        # start r from 1 since we always compare arr[R] with arr[R - 1]
        for R in range(1, n):
            if arr[R] == arr[R - 1]:
                # equal -> turbulence breaks, start new window at R
                L = R
            else:
                # for R >= 2, check if pattern breaks at position R
                if R == 1:
                    pass
                else:
                    # if it is not a peak or valley, reset window R - 1:
                    if not ((arr[R - 2] < arr[R - 1] > arr[R]) or 
                            (arr[R - 2] > arr[R - 1] < arr[R])):
                            L = R - 1
            
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen