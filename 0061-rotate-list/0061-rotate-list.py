# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        fast = head
        l = 1
        while fast.next:
            fast = fast.next
            l += 1

        fast.next = head

        slow = head
        for i in range(l - (k%l)):
            fast = fast.next

        new_head = fast.next
        fast.next = None 
        return new_head