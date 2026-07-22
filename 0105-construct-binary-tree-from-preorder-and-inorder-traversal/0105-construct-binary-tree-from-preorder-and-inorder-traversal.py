# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # idea: preorder[0] will be the root of the tree. 
        # once we find this value in inorder (call it mid), anything to the left of it is on its left subtree and anything to the right of it is on its right subtree.
        # if we apply a recursive algo where we split the list and build the left subtree based on preorder[1:mid + 1] and inorder[:mid] and the right subtree based on preorder[mid + 1:] and inorder[mid + 1:], then we can create the tree

        if not preorder or not inorder:
            return None
        
        value = preorder[0]
        mid = inorder.index(value)
        node = TreeNode(value)

        node.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return node