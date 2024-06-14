# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def predecessor(rn: TreeNode) -> TreeNode:
            while rn and rn.left:
                rn = rn.left
            return rn

        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not (root.left or root.right):
                root = None
            elif not root.left and root.right:
                root = root.right
            elif root.left and not root.right:
                root = root.left
            else:
                lr = predecessor(root.right)
                lr.left = root.left
                root = root.right
        return root
