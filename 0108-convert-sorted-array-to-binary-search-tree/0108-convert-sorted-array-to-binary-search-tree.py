# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def add_node(start, end):
            if end == start:
                return 
            mid = (end+start)//2
            root = TreeNode(nums[mid])
            root.left = add_node(start, mid)
            root.right = add_node(mid+1, end)
            return root


        n = len(nums) 
        if n == 1:
            return TreeNode(nums[0])
        return add_node(0, n)
