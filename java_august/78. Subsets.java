class Solution {
    private List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        answer.add(new ArrayList<Integer>());
        backtrack(new ArrayList<Integer>(), 0, n, nums);
        return answer;
    }

    private void backtrack(List<Integer> tmp, int idx, int n, int[] nums) {
        if (idx >= n) {
            return;
        }
        for (int i=idx; i<n; i++){
            tmp.add(nums[i]);
            answer.add(new ArrayList<>(tmp));
            backtrack(tmp, i+1, n, nums);
            tmp.remove(tmp.size()-1);
        }
    }
}