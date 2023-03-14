# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def add(n, l):
            if l is None:
                return 0
            n = n * 10 + l.val
            if not l.left  and not l.right:
                return n
            return add(n, l.left) + add(n, l.right)
        return add(0, root)
    
        
        