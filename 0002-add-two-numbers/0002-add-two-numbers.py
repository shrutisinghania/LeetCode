# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addList(l, l1, l2, c):
            if not l1 and not l2:
                if c:
                    l.next = ListNode(c)
                return
            elif not l1:
                val = l2.val + c
                l2.val = val % 10
                c = val // 10
                l.next = l2
                return addList(l.next, l1, l2.next, c)
            elif not l2:
                val = l1.val + c
                l1.val = val % 10
                c = val // 10
                l.next = l1
                return addList(l.next, l1.next, l2, c)
            
            val = l1.val + l2.val + c
            l1.val = val % 10
            c = val // 10
            l.next = l1
            return addList(l.next, l1.next, l2.next, c)
        
        l = ListNode()
        addList(l, l1, l2, 0)
        return l.next

            
