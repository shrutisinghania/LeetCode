# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = [(root, root.val, root.val)]
        a = 0
        while q:
            n, mi, ma = q.pop(0)
            a = max(a, abs(n.val - mi), abs(n.val - ma))
            if n.left:
                q.append((n.left, min(mi, n.val), max(ma, n.val)))
            if n.right:
                q.append((n.right, min(mi, n.val), max(ma, n.val)))
        return a
                