class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # initiate res and queue and pointers        
        res = []
        q = collections.deque()
        l = r = 0

        # iterate r pointer while it is less than len nums
        while r < len(nums):
            # while queue exists and last element of queue is less than val at r
            while q and nums[q[-1]] < nums[r]:
                # pop
                q.pop()

            # append current r index
            q.append(r)

            # keep the k window size
            if l > q[0]:
                q.popleft()
            
            # if r is greater than or equal to k
            if r + 1 >= k:
                # append the val of 0 index of queue
                res.append(nums[q[0]])
                # increment left pointer
                l += 1
            # increment right pointer
            r += 1
        # return res
        return res

    
