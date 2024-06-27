# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # if not root.left and not root.right:
        #     return root
        
        leftNode = root.left
        rightNode = root.right
        root.left = self.invertTree(rightNode)
        root.right = self.invertTree(leftNode)
        return root
