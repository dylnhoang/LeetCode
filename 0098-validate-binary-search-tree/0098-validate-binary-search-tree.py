# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(float('-inf'), float('inf'), root)
    
    def valid(self, min, max, node):
        if not node:
            return True

        if not (node.val < max and node.val > min):
            return False
        
        return self.valid(node.val, max, node.right) and self.valid(min, node.val, node.left)
