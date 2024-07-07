# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def find_depth(self, root):
            if not root:
                return [0,0]
            if not root.left and not root.right:
                return [0, 0]
            l, r = 0, 0
            if root.left:
                l = max(find_depth(self, root.left)) + 1
            if root.right:
                r = max(find_depth(self, root.right)) + 1
            self.max = max(l + r, self.max)
            return [l, r]
        
        find_depth(self, root)
        return self.max