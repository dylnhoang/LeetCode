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
        oldToCopy = {}

        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            newNode = Node(node.val)
            oldToCopy[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
            
        return dfs(node) if node else None
