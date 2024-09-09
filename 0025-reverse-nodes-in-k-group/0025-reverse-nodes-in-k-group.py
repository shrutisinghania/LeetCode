# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
            
        def rev(head, node, kn):
            if not head:
                return
            curr = head
            prev = None
            h = 0
            for i in range(kn):
                if not curr:
                    rev(prev, node, h)
                    return
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                h += 1
            node.next = prev
            rev(curr, head, kn)
        
        
        new_node = ListNode()
        rev(head, new_node, k)
        
        return new_node.next
        
                