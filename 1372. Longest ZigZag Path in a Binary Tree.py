# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def maxZZ(node: TreeNode, goLeft, length) -> int:
            nonlocal max_length
            
            if not node:
                return
            max_length = max(max_length, length)

            if goLeft:
                maxZZ(node.left, False, length + 1)
                maxZZ(node.right, True, 1)
            else:
                maxZZ(node.left, False, 1)
                maxZZ(node.right, True, length + 1)
        
        max_length = 0
        maxZZ(root, True, 0)
        maxZZ(root, False, 0)
        return max_length