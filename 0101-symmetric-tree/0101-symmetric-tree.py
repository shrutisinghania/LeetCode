# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def find(l, r):
            if not l and not r:
                return True
            if not r or not l:
                return False
            if l.val != r.val:
                return False
            return find(l.left, r.right) and find(l.right, r.left)
        
        return find(root.left, root.right)
        