# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        

        def trav(r):
            nonlocal d
            if not r:
                return 0
            if not r.left and not r.right:
                d = max(d, r.val)
                return r.val 
            l = trav(r.left)
            ri = trav(r.right)
            d = max(d, r.val + l + ri)
            d = max(d,r.val, r.val + max(l, ri) )
            return max(r.val, r.val + max(l, ri))
        
        d = root.val
        trav(root)
        return d