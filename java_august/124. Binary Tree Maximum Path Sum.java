/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int maxSum;

    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        getMax(root);
        return maxSum;
    }

    private int getMax(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = Math.max(getMax(node.left), 0);
        int right = Math.max(getMax(node.right), 0);

        maxSum = Math.max(maxSum, node.val + left + right);

        return node.val + Math.max(left, right);
    }
}