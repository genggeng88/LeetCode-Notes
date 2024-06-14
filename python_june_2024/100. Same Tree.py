# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        def check(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return True
        
        while queue:
            node1, node2 = queue.popleft()
            if not check(node1, node2):
                return False
            if node1:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
