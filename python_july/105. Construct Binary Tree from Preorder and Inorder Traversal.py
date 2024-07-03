# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(preorder[0])
        for idx in range(n):
            if inorder[idx] == root.val:
                break

        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root        