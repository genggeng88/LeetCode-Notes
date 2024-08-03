class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = nums[0];

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        heap.offer(new int[] {result[0], 0});

        for (int i=1; i<n; i++) {
            while (!heap.isEmpty() && heap.peek()[1] < i-k) {
                heap.poll();
            }
            result[i] = nums[i] + heap.peek()[0];
            heap.offer(new int[] {result[i], i});
        }
        return result[n-1];
    }
}