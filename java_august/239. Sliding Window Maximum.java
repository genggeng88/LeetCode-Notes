class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        Deque<int[]> heap = new LinkedList<>();
        heap.addFirst(new int[] {nums[0], 0});
        int[] result = new int[n-k+1];

        for (int i=0; i < n; i++) {
            while (heap.size() > 0 && heap.peekFirst()[1] <= i - k) {
                heap.removeFirst();
            }
            int curr = nums[i];
            while (heap.size() > 0 && heap.peekLast()[0] < curr) {
                heap.removeLast();
            }
            heap.addLast(new int[] {curr, i});
            if (i >= k-1) {
                result[i-k+1] = heap.peekFirst()[0];
            }
        }
        return result;
    }
}