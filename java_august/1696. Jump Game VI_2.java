class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = nums[0];

        Deque<Integer> deque = new LinkedList<>();
        deque.offerLast(0);

        for (int i=1; i<n; i++) {
            while (!deque.isEmpty() && deque.peekFirst() < i-k) {
                deque.pollFirst();
            }
            result[i] = nums[i] + result[deque.peekFirst()];
            while (!deque.isEmpty() && result[deque.peekLast()] < result[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);
        }
        return result[n-1];
    }
}