# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre_list: List[int], in_list: List[int]) -> Optional[TreeNode]:
        if len(in_list) == 0:
            return None
        node = pre_list.pop(0)
        index = in_list.index(node)
        head = TreeNode(node)
        head.left = self.buildTree(pre_list, in_list[:index])
        head.right = self.buildTree(pre_list, in_list[index + 1:])
        return head
    
        