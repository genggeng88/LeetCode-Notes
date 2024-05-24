# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def preorder(node: TreeNode, prefix):
            nonlocal ans

            if not node:
                return 
            # a leaf
            if not (node.left or node.right):
                ans += prefix * 10 + node.val
            if node.left:
                preorder(node.left, prefix*10 + node.val)
            if node.right:
                preorder(node.right, prefix*10 + node.val) 

        ans = 0
        preorder(root, 0)
        return ans