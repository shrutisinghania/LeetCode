# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        curr = d 
        nxt = head
        for i in range(n):
            nxt = nxt.next
        while nxt:
            curr = curr.next
            nxt = nxt.next
        curr.next = curr.next.next
        return d.next        
