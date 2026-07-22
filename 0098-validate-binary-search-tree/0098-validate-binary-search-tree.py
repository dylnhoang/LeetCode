# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(float('-inf'), float('inf'), root)

    # we implement a helper method that keeps track of the current min, current max, and the node we want to check the validity of
    # if we go left, we change the current max value; if we go right, we change the current min value
    def valid(self, min, max, node):
        if not node: 
            return True
        elif node.val <= min or node.val >= max:
            return False
        else:
            return self.valid(min, node.val, node.left) and self.valid(node.val, max, node.right)
