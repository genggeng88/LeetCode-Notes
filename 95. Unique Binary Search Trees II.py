# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def tree(low: int, high: int) -> List[Optional[TreeNode]]:
            if low > high:
                return [None]
            ans = []
            for i in range(low, high + 1):
                left_trees = tree(low, i - 1)
                right_trees = tree(i + 1, high)
                for l in left_trees:
                    for r in right_trees:
                        head = TreeNode(i)
                        head.left = l
                        head.right = r
                        ans.append(head)
            return ans

        return tree(1, n)