class Solution {
    public int mostFrequentEven(int[] nums) {
        //Map<num, frequency>
        int n = nums.length;
        Map<Integer, Integer> mapping = new HashMap<>();
        List<Integer> evens = new ArrayList<>();
       
        for(int i=0; i<n; i++){
            if(nums[i]%2==0){
                evens.add(nums[i]);
                if(mapping.get(nums[i])==null){
                    mapping.put(nums[i], 1);
                }
                else{
                    mapping.put(nums[i], mapping.get(nums[i])+1);
                }
                
            }
        }
        if (evens.size()==1){
            return evens.get(0);
        }
        int outcome=-1;
        int count=0;
        int m = evens.size();
        Collections.sort(evens);
        for(int j=0; j<m; j++){
            if(mapping.get(evens.get(j)) > count){
                count = mapping.get(evens.get(j));
                outcome = evens.get(j);
            }
        }
        return outcome;
    }
}