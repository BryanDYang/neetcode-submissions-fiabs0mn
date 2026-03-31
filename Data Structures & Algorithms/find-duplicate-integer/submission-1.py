class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow = fast = nums

        # while fast and fast.next:

        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         return slow
            
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow



