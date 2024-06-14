# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        idx = 1
        queue = deque([root])
        maximal = root.val
        
        while queue:
            sumval = 0
            level_length = len(queue)
            level += 1
            for i in range(level_length):
                node = queue.popleft()
                sumval += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if sumval > maximal:
                maximal = sumval
                idx = level
        
        return idx