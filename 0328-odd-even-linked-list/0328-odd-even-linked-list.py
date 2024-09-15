# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even = head
        odd = head.next
        odd_head = odd
        while even and odd and odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            odd = odd.next
        even.next = odd_head
        return head
