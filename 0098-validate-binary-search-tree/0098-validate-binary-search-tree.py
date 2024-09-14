# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def checkBST(node, minimum, maximum):
            if not node:
                return True
            if minimum >= node.val or node.val >= maximum :
                return False
            return checkBST(node.left, minimum,node.val) and checkBST(node.right, node.val, maximum)

        return checkBST(root, float("-inf"), float("inf"))