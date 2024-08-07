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
    public TreeNode sortedArrayToBST(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return null;
        }
        if (n == 1) {
            return (new TreeNode(nums[0]));
        }
        TreeNode node = new TreeNode(nums[n/2]);
        node.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, n / 2));
        node.right = sortedArrayToBST(Arrays.copyOfRange(nums, n/2+1, n));
        return node;
    }
}