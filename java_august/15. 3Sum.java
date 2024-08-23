class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> answer = new ArrayList<>();
        for (int i=0; i<n && nums[i] <= 0; i++) {
            if (i == 0 || nums[i-1] != nums[i]) {
                twoSum(nums, i, answer);
            }
        }
        return answer;
    }

    public void twoSum(int[] nums, int i, List<List<Integer>> answer) {
        int lo = i+1, hi = nums.length-1;
        while (lo < hi) {
            int sum = nums[i] + nums[lo] + nums[hi];
            if (sum == 0) {
                answer.add(Arrays.asList(nums[i], nums[lo++], nums[hi--]));
                while (lo < hi && nums[lo] == nums[lo-1]) {
                    lo++;
                }
            }
            else if (sum < 0) {
                lo++;
            }
            else{
                hi--;
            }
        }
    }
}