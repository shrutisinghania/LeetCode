# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node or not node.next:
            return node
        head = node
        res = head
        curr = node.next
        while curr:
            if curr.val == head.val:
                curr = curr.next
                head.next = None
                continue
            head.next = curr 
            head = head.next
            curr = curr.next
        return res
