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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        Pair<TreeNode, Integer> p = new Pair<>(root, 1);
        stack.push(p);
        int res = 0;

        while (!stack.isEmpty()){
            Pair<TreeNode, Integer> tmp = stack.pop();
            TreeNode node = tmp.first;
            Integer depth = tmp.second;
            res = Math.max(res, depth);
            if (node.right != null) {
                stack.push(new Pair<>(node.right, depth+1));
            }
            if (node.left != null) {
                stack.push(new Pair<>(node.left, depth+1));
            }
        }
        return res;
    }
}

class Pair<T, U> {
    public T first;
    public U second;

    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }
}