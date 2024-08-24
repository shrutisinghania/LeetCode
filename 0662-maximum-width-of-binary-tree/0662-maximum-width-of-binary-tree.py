# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_info = defaultdict(list)
        
        def get_level_info(root, level, n):
            if not root:
                return
            level_info[level].append(n)
            get_level_info(root.left, level+1, 2*n+1)
            get_level_info(root.right, level+1, 2*n+2)
        
        get_level_info(root, 0, 0)
        max_width = 0
        for key, value in level_info.items():
            width = value[-1] - value[0] + 1
            max_width = max(max_width, width)
        return max_width