# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        stack = [root]
        while stack:
            node = stack.pop()
            vals.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        vals.sort()
        res = math.inf
        for i in range(1,len(vals)):
            res = min(res, vals[i]-vals[i-1])
        return res