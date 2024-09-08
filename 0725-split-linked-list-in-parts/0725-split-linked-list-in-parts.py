# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        n = len(l)
        rem = n % k
        q = n // k
        res = []
        i = 0
        for _ in range(k):
            maxrange = i + q - 1
            if rem > 0:
                maxrange += 1
                rem -= 1
            if i < len(l):
                l[maxrange].next = None
                res.append(l[i])
            else:
                res.append(None)
            i = maxrange + 1
        return res
