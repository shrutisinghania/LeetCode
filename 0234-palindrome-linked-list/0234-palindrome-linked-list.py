# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        l = []
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                l.append(slow.val)
            slow = slow.next
            
        while slow:
            e = l.pop()
            if e != slow.val:
                return False
            slow = slow.next
        return True


        
