# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        def validate(node, left, right): #node, left bound, right bound
            if node == None:
                return True
            if not left < node.val < right:
                return False
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)

        return validate(root, float('-inf'), float('inf'))
        