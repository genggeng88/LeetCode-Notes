class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int[] result = new int[2];
        Map<Integer, Integer> met = new HashMap<>();
        for(int i = 0; i<n; i++){
            if(met.get(target - numbers[i]) != null){
                result[0] = met.get(target - numbers[i])+1;
                result[1] = i+1;
            }
            else{
                met.put(numbers[i], i);
            }
        }
        return result;
    }
}