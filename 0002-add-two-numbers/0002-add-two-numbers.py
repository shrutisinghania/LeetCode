# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        l = ListNode()
        res = l
        while l1 or l2 or c:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
                
            val += c
            t = ListNode(val % 10)
            c = val // 10
            
            l.next = t
            l = l.next
        return res.next
            
            
            
            