# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
            
        def bfs(node, level):
            if not node:
                return
            
            if level == len(l):
                l.append(node.val)
            else:
                l[level] += node.val

            bfs(node.left, level+1)
            bfs(node.right, level+1)

            
        l = []
        bfs(root, 0)
        return l.index(max(l)) + 1