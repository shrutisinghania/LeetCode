# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if not head:
            return head
        fast = head
        slow = head
        for i in range(k):
            if not fast.next:
                return self.rotateRight(head, k % (i+1))
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None 
        fast.next = head
        return new_head