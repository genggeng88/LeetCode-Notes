# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque([root])
        acc = 0
        while stack:
            node = stack.pop()
            acc += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return acc