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

    private int maxDiameter;

    public int diameterOfBinaryTree(TreeNode root) {
        maxDiameter = 0;
        helper(root);
        return maxDiameter;
    }

    public int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftD = helper(root.left);
        int rightD = helper(root.right);

        maxDiameter = Math.max(maxDiameter, leftD+rightD);

        return Math.max(leftD, rightD) + 1;
    }
}