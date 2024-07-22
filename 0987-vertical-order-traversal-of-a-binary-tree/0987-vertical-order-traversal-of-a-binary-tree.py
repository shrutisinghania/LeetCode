# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def findDepth(self, root, c, r):
            if not root:
                return
            self.d[c].append((root.val, r))
            findDepth(self, root.left, c - 1, r+1)
            findDepth(self, root.right, c + 1, r+1)            
        
        self.d = defaultdict(list)
        findDepth(self, root, 0, 0)
        k = sorted(self.d)
        res = []
        for i in k:
            l = []
            for a, b in sorted(self.d[i], key=lambda tup: (tup[1], tup[0])):
                l.append(a)
            res.append(l)
        return res
        