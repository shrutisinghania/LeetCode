# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        A = headA
        B = headB
        while headA != headB:
            headA = headA.next if headA else B
            headB = headB.next if headB else A
        return headA
        