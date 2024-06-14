# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(curr_node: TreeNode) -> bool:
            nonlocal ans

            if not curr_node:
                return False
            
            left = dfs(curr_node.left)
            right = dfs(curr_node.right)

            mid = curr_node == p or curr_node == q

            if left + right + mid >= 2:
                ans = curr_node
            
            return left or right or mid
        
        ans = None
        dfs(root)
        return ans
