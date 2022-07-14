# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = []
        if root:
            level = [root]
        else:
            level = []
        while level:
            ans.append(level[-1].val)
            curr = level
            level = []
            for i in curr:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
        return ans
    
  