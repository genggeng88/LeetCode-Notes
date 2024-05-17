class Solution {
    public boolean findTarget(TreeNode root, int k) {
        if(root.val == 2*k){
            return false;
        }
        Set<Integer> met = new HashSet<>();
        Queue<TreeNode> queue = new LinkedList<>();
        met.add(root.val);
        queue.add(root);

        while(!queue.isEmpty()){
            TreeNode top = queue.remove();
            if(top.left == null && top.right == null){
                continue;
            }
            if(top.left != null){
                if(met.contains(k-top.left.val)){
                    return true;
                }
                queue.add(top.left);
                met.add(top.left.val);
            }
            if(top.right != null){
                if(met.contains(k-top.right.val)){
                    return true;
                }
                queue.add(top.right);
                met.add(top.right.val);
            }
        }
        return false;    
    }
}