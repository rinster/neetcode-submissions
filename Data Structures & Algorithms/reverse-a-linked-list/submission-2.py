# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # ref pointer to next node, so we don't lose it
            curr.next = prev # point it's previous node
            prev = curr # move pointer forward
            curr = temp
        
        return prev