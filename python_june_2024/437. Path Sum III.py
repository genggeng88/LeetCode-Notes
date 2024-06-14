# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def preorder(node: TreeNode, curr_sum: int):
            nonlocal cnt
            if not node:
                return
            curr_sum += node.val

            if curr_sum == k:
                cnt += 1
            cnt += h[curr_sum - k]
            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1            
                
        cnt, k = 0, targetSum
        h = defaultdict(int)
        preorder(root, 0)
        return cnt