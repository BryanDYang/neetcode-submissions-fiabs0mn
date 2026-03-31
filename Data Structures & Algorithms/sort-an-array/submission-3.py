class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # helper function to merge the arrays with three pointers
        def merge(arr, L, M, R):
            # initiate the left and array slices
            left, right = arr[L:M + 1], arr[M+1:R+1]

            # initiate the pointers
            i, j, k = L, 0, 0

            # while left & right pointer is less than the respective arrays
            # this condition only executes when both arrays have values (not either one)
            while j < len(left) and k < len(right):
                # if left array value is less than or equal to right array value
                if left[j] <= right[k]:
                    # place the left value at the original array pointer 
                    arr[i] = left[j]
                    # increment the left pointer
                    j += 1
                # else (i.e. if right array value is less than the left array value)
                else:
                    # place the right value at the original array pointer
                    arr[i] = right[k]
                    # increment the right pointer
                    k += 1
                # regardless which one is smaller increment the original array pointer
                # for the next iteration of comparison
                i += 1
            
            # after one of the arrays (left or right or both)
            # we want to fill the rest of the original pointer with 
            # left or right array 
            # while left pointer is less than 
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        # helper function to travese down to each node level
        def mergeSort(arr, l, r):
            # if left and right node pointers are same return since they are merged
            # base case
            if l == r:
                return

            # middle node 
            m = (l + r) // 2
            # recursive call of merge sort on the array from left to middle
            # going down to node level
            mergeSort(arr, l, m)

            # recursive call of merge sort on the arrya from middle+1 to right
            # going down to node level
            mergeSort(arr, m + 1, r)

            # merge all the nodes with three pointers 
            merge(arr, l, m, r)

            # return when finished. No need to return nums since this
            # is change in place but we can also just return array so
            # we don't have to manually return the array outside of the function
            return

        # using the merge sort & return the array
        mergeSort(nums, 0, len(nums) + 1)

        return nums


