class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> unique = new HashSet<>();
        int len = nums.length;
        for(int i=0; i<len; i++){
            if (unique.contains(nums[i])){
                return true;
            }
            unique.add(nums[i]);
        }
        return false;
    }
}