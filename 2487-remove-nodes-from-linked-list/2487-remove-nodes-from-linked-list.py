# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nxt = self.removeNodes(head.next)
        if head.val < nxt.val:
            return nxt
        head.next = nxt
        return head
            