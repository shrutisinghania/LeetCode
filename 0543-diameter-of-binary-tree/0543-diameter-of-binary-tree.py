# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m = 0
        def r(root):
            if not root:
                return 0
            left = r(root.left)
            right = r(root.right)
            self.m = max(self.m, left+right)
            return max(left, right) + 1
        r(root)
        return self.m
        