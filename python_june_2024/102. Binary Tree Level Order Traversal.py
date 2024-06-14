# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not (root.left or root.right):
            return [[root.val]]
        
        stack = deque([root])
        ans = []
        while stack:
            level_len = len(stack)
            tmp = []
            for i in range(level_len):
                node = stack.popleft()
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(tmp)
        return ans