# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_most(root)
    
    def left_most(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        smallest_node = self.stack.pop()
        if smallest_node.right:
            self.left_most(smallest_node.right)
        return smallest_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()