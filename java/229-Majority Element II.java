class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n = nums.length;
        int thres = n/3;
        List<Integer> spare = new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> mapping = new HashMap<>();

        for(int i = 0; i<n; i++){
            if (mapping.get(nums[i]) != null){
                mapping.put(nums[i], mapping.get(nums[i])+1);
            }
            else{
                mapping.put(nums[i], 1);
                spare.add(nums[i]);
            }
        }

        int m = spare.size();
        for(int j = 0; j<m; j++){
            if(mapping.get(spare.get(j)) > thres){
                result.add(spare.get(j));
            }
        }

        return result;
    }
}