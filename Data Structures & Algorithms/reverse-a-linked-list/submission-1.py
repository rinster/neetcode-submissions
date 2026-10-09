# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        # base case nothing to reverse
        if not curr:
            return None
        
        # single node list already reversed; it is the new head
        if not curr.next:
            return curr

        #recursively reverse the rest of the list
        newHead = self.reverseList(curr.next)

        # curr.next is now the LAST node of the reversed tail.
        # Point it back to curr to complete the reversal at this level.
        curr.next.next = curr

        # curr is now the tail of the reversed portion
        curr.next = None
        
        # pass the new head all the way back up
        return newHead
