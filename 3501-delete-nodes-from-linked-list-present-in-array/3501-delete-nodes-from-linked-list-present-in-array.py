# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        for i in nums:
            d[i] = None
        res = ListNode()
        res.next = head
        prev = res
        while head:
            if head.val in d.keys():
                prev.next = head.next
                head = head.next
                continue
            head = head.next
            prev = prev.next
            
        return res.next
        