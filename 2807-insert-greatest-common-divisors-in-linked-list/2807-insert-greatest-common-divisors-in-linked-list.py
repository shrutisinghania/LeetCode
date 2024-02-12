# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insertNode(a, b, val):
            l = ListNode(val, b)
            a.next = l
            return b
        
        def gcd(a, b):
            for n in range(min(a, b), 0, -1):
                if a%n == 0 and b%n == 0:
                    return n
        
        
        p = head    
        while head.next != None:
            a = head
            b = head.next
            val = gcd(a.val, b.val)
            head = insertNode(a, b, val)
        return p
            
        