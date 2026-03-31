# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create a dummy node before head
        dummy = ListNode(0, head)
        # set a pointer for group prev
        groupPrev = dummy

        while True:
            # get the kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            # next group start node is kth next node
            groupNext = kth.next

            # reversing kth nodes
            # making it easy by setting prev and curr nodes
            # kth.next node should be prev to reverse and link back to the list
            # groupPrev.next should be curr node
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # old head (now tail) of the reversed group
            tmp = groupPrev.next
            # connects dummy to the new head of the first reversed group
            groupPrev.next = kth
            # move groupPrev to the tail for the next round
            groupPrev = tmp

        return dummy.next

    # helper function returning kth nodes
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
