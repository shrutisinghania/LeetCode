# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        oq = [original]
        cq = [cloned]
        while oq:
            n = oq.pop(0)
            cn = cq.pop(0)
            if n == target:
                return cn
            if n.left:
                oq.append(n.left)
                cq.append(cn.left)
            if n.right:
                oq.append(n.right)
                cq.append(cn.right)
    
        