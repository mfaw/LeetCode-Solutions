# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            rootValue = preorder.pop(0)
            rootIndex = inorder.index(rootValue)
            root = TreeNode(inorder[rootIndex])
            root.left = self.buildTree(preorder, inorder[:rootIndex])
            root.right = self.buildTree(preorder, inorder[rootIndex+1:])
			
            return root
        