class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        for (int i=0; i<n; i++) {
            result[i] = -1;
        }
        
        Stack<Integer> stack = new Stack<>();
        
        for (int i=0; i<2*n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i%n]) {
                int idx = stack.pop();
                result[idx] = nums[i%n]; 
            }
            if (i < n) {
                stack.push(i);
            }
        }

        return result;
    }
}