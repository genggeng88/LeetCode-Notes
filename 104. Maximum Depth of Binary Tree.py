# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # go DFS, update the depth when meeting larger depth

        if not root:
            return 0
        queue = deque([(root, 0)])
        ans = 0
        visited = []
        while queue:
            node, depth = queue.popleft()
            ans = max(ans, depth + 1)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return ans