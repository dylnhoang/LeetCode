# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(root):
            if root == None:
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            #computing split path from current root; leftMax or rightMax will be 0 if negative, so will technically be a oneliner
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax) #returns best straight line path from root

        dfs(root)
        return res[0]



        