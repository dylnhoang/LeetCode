# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we use an array to store our result so we can access it within our dfs method easily
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            leftMax = max(0, dfs(node.left)) # determine the path from the left node that yields the max value WITHOUT splits
            rightMax = max(0, dfs(node.right)) # determine the path from the left node that yields the max value WITHOUT splits

            res[0] = max(res[0], leftMax + node.val + rightMax) # check if you can yield a max value by splitting at the current node
            return node.val + max(leftMax, rightMax) # return the max value you can get at this node (you must include the node) without splitting 

        dfs(root)
        return res[0]