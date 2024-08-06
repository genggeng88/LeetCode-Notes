class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length(), farthest = 0;
        if (s.charAt(n-1) == '1') {
            return false;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        while (queue.size() > 0) {
            int idx = queue.poll();
            int start = Math.max(idx+minJump, farthest+1);
            int end = Math.min(idx+maxJump, n-1);

            for (int i=start; i <= end; i++) {
                if (s.charAt(i) == '0') {
                    if (i == n-1) {
                        return true;
                    }
                    queue.offer(i);
                }
            }
            farthest = idx + maxJump;
        }
        return false;
    }
}