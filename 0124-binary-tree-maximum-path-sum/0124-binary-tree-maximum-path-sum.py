# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax, rightMax = max(0, dfs(node.left)), max(0, dfs(node.right))

            res[0] = max(res[0], leftMax + rightMax + node.val)

            return node.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]

        