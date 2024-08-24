# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def findDepth(root, c, r):
            if not root:
                return
            d[c].append((r, root.val))
            findDepth(root.left, c-1, r+1)
            findDepth(root.right, c+1, r+1)
           
        findDepth(root, 0, 0)
        res = []
        for i in sorted(d):
            l = []
            for a, b in sorted(d[i]):
                l.append(b)
            res.append(l)
        return res