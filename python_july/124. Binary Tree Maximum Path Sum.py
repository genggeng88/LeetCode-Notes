# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        self.helper(root)
        return self.max_sum

    def helper(self, node):
        if not node:
            return 0
        
        leftSum = max(self.helper(node.left), 0)
        rightSum = max(self.helper(node.right), 0)

        inorder = node.val + leftSum + rightSum
        self.max_sum = max(self.max_sum, inorder)

        return node.val + max(leftSum, rightSum)