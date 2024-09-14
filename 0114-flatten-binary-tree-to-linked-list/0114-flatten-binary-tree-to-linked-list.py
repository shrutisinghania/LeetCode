# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return
        head = root
        while head:
            if head.left:
                temp = head.left
                while temp and temp.right:
                    temp = temp.right
                temp.right = head.right
                head.right = head.left
                head.left = None
            head = head.right


        
        