# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        queue = deque([root])
        ans = []
        odd = True
        while queue:
            length = len(queue)
            tmp = []
            for _ in range(length):
                node = queue.popleft()
                tmp.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if odd:
                ans.append(reversed(tmp))
            else:
                ans.append(tmp)
            odd = not odd
        return ans