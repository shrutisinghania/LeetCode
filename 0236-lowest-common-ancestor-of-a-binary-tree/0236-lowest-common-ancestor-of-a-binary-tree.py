# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not node or node == p or node == q:
            return node
        a = self.lowestCommonAncestor(node.left, p, q)
        b = self.lowestCommonAncestor(node.right, p, q)
        if a and b:
            return node
        return a or b
