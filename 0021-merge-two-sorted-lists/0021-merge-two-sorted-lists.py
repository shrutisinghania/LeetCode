# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        def findMin(l, l1, l2):
            if not l1 and not l2:
                return 
            if not l1:
                l.next = l2
                findMin(l.next, l1, l2.next) 
                return
            if not l2:
                l.next = l1
                findMin(l.next, l1.next, l2) 
                return
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            findMin(l.next, l1, l2) 
                
        res = ListNode()
        findMin(res, list1, list2)
        return res.next

                