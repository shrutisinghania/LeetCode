# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)

        if not head.next:
            return head

        curr = head

        while curr.next:
            node = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = node
            curr = curr.next.next

        return head
