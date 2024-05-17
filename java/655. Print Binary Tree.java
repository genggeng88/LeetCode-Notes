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
    public List<List<String>> printTree(TreeNode root) {
        List<List<String>> res = new ArrayList<>();
        int m = DFS(root)+1;
        int n = (int)Math.pow(2, m) - 1;
        
        if(root == null){
            return null;
        }
        for(int i = 0; i<m; i++){
            List<String> el = new ArrayList<>();
            for(int j= 0; j<n; j++){
                el.add("");
            }
            res.add(el);
        }
        Queue<Pack> queue = new LinkedList<>();
        Pack p = new Pack(0, (n-1)/2, root);
        queue.add(p);

        while(!queue.isEmpty()){
            Pack top = queue.remove();
            int r = top.r, c = top.c;
            res.get(r).set(c, Integer.toString(top.root.val));
            if(top.root.left != null){
                queue.add(new Pack(r+1, c-(int)Math.pow(2, m-r-2), top.root.left));
            }
            if(top.root.right != null){
                queue.add(new Pack(r+1, c+(int)Math.pow(2, m-r-2), top.root.right));
            }
        }
        return res;
    }

    public class Pack{
        int r, c, start, end;
        TreeNode root;
        public Pack(int r, int c, TreeNode root){
            this.r = r;
            this.c = c;
            this.root = root;
        }
    }

    public int DFS(TreeNode root){
        int height = 0;

        if(root.left == null && root.right == null){
            return height;
        }
        else if(root.left == null && root.right != null){
            return 1 + DFS(root.right);
        }
        else if(root.left != null && root.right == null){
            return 1 + DFS(root.left);
        }
        return 1 + Math.max(DFS(root.left), DFS(root.right));
        
    }
}








