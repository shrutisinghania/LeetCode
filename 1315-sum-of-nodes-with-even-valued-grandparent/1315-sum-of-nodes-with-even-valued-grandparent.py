# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0
        q = [root]
        l = []
        while q:
            n = q.pop(0)
            if n.val %2 == 0:
                l.append(n.left)
                l.append(n.right)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        s = 0
        l = [i for i in l if i != None] 
        for i in l:
            if i.left:
                s += i.left.val
            if i.right:
                s += i.right.val
        return s