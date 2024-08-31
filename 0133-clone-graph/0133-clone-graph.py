"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        d = {}
        q = [node]
        d[node.val] = Node(node.val)
        while q:
            n = q.pop(0)
            for i in n.neighbors:
                if i.val not in d.keys():
                    q.append(i)
                    d[i.val] = Node(i.val)
                d[n.val].neighbors.append(d[i.val])
             
        return d[node.val]