# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = []
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        rem = n % k
        q = n // k
        res = []
        
        curr = head
        nxt = head
        for _ in range(k):
            maxrange = q
            if rem > 0:
                maxrange += 1
                rem -= 1
            if curr:
                res.append(curr)
            else:
                res.append(None)
                continue
            for _ in range(maxrange-1):
                curr = curr.next
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
        return res
