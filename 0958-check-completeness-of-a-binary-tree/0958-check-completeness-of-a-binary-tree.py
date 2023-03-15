# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append(root)
        while queue[0] is not None:
            node = queue.popleft()
            queue.append(node.left)
            queue.append(node.right)
        while queue and queue[0] is None:
            queue.popleft()
        return not queue