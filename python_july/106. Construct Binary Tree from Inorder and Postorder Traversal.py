# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base cases
        n = len(inorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        for i in range(n):
            if inorder[i] == root.val:
                break

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root