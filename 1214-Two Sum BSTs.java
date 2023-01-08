class Solution {
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        Set<Integer> first = new HashSet<>();
        Queue<TreeNode> tree1 = new LinkedList<>();
        Queue<TreeNode> tree2 = new LinkedList<>();
        tree1.add(root1);
        first.add(target - root1.val);
        tree2.add(root2);

        while(!tree1.isEmpty()){
            TreeNode top = tree1.remove();
            if(top.left == null && top.right == null){
                continue;
            }
            if(top.left != null){
                tree1.add(top.left);
                first.add(target - top.left.val);
            }
            if(top.right != null){
                tree1.add(top.right);
                first.add(target - top.right.val);
            }
        }

        while(!tree2.isEmpty()){
            TreeNode top = tree2.remove();
            if(first.contains(top.val)){
                return true;
            }
            if(top.left == null && top.right == null){
                continue;
            }
            if(top.left != null){
                tree2.add(top.left);
            }
            if(top.right != null){
                tree2.add(top.right);
            }
        }

        return false;
    }
}