# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(gp, p, node):
            if not node:
                return
            if gp % 2 == 0:
                self.sum += node.val
            if node.left:
                dfs(p, node.val, node.left)
            if node.right:
                dfs(p, node.val, node.right)


        dfs(-1, -1, root)
        return self.sum