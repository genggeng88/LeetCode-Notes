# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, -float('inf'))]
        cnt = 0
        
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                cnt += 1
            if node.left:
                stack.append([node.left, max(max_so_far, node.val)])
            if node.right:
                stack.append([node.right, max(max_so_far, node.val)])
        return cnt
        