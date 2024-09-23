"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = [root]
        while q:
            l = len(q)
            prev = None
            while l:
                node = q.pop(0)
                if node.left:
                    if prev:
                        prev.next = node.left
                    prev = node.left
                    q.append(node.left)
                if node.right:
                    if prev:
                        prev.next = node.right
                    prev = node.right
                    q.append(node.right)
                    
                l -= 1
        return root