# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isSub(h, r):
            if not h:
                return True
            if not r:
                return False
            if h.val != r.val:
                return False
            return isSub(h.next, r.left) or isSub(h.next, r.right)
           
        
        def traverseTree(he, ro):
            if not ro or not he:
                return
            if he.val == ro.val:
                if isSub(he, ro):
                    return True
            return traverseTree(he, ro.left) or traverseTree(he, ro.right)

        return traverseTree(head, root)
    
