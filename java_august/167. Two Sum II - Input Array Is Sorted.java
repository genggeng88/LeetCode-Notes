class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int i=0, j=n-1;

        while (i < j) {
            int currSum = numbers[i] + numbers[j];
            if (currSum == target) {
                return new int[]{i+1, j+1};
            }
            else if (currSum < target) {
                i += 1;
            }
            else {
                j -= 1;
            }
        }
        return new int[2];
    }
}