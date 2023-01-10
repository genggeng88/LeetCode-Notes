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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        int k = 0, n=nums.length;
        if(n==0){
            return null;
        }
        int max = nums[k];
        for(int i= 1; i<n; i++){
            if(nums[i] > max){
                max = nums[i];
                k = i;
            }
        }
        TreeNode root = new TreeNode(max);
        root.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums, 0, k));
        root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, k+1, n));
        return root;
    }
}