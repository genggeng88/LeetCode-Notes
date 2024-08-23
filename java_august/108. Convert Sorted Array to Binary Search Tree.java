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
        int idx = n/2;
        int rootVal = nums[idx];
        TreeNode root = new TreeNode(rootVal);
        if (n == 1) {
            return root;
        }
        root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, idx));
        root.right =  sortedArrayToBST(Arrays.copyOfRange(nums, idx+1, n));

        return root;
    }
}