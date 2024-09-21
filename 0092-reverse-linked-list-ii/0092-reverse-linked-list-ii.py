# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head
        
        def rev(head_node, i):
            curr = head_node
            prev = None
            while i:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp 
                i -= 1
            head_node.next = curr
            return prev
        
        new_head = ListNode()
        new_head.next = head
        node = new_head
        i = 0
        while i < left - 1:
            node = node.next
            i += 1
        node.next = rev(node.next, right - left + 1)
        return new_head.next