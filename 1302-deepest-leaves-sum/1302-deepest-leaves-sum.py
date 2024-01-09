# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        s = 0
        while len(q):
            qlen = len(q)
            s = 0
            for _ in range(qlen):
                n = q.pop(0)
                s += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return s