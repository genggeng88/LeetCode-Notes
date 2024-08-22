class Solution {
    private List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        backtrack(new ArrayList<Integer>(), 1, k, n);
        return answer;
    }

    public void backtrack(List<Integer> tmp, int start, int rem, int target) {
        if (target < 0) {
            return;
        }
        if (rem == 0) {
            if (target == 0) {
                answer.add(new ArrayList<>(tmp));
            }
            return;
        }

        for (int i=start; i<11-rem; i++) {
            tmp.add(i);
            backtrack(tmp, i+1, rem-1, target-i);
            tmp.remove(tmp.size()-1);
        }
    }
}