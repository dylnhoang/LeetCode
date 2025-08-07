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
        oldToCopy = {} # past nodes to clone node

        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            copy = Node(node.val)
            oldToCopy[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) #create clones of neighbors, then connect
            
            return copy

        return dfs(node) if node else None #handles edge case of initial node being nonexistent
