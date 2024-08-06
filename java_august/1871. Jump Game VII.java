class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length(), sum = 0;
        int[] reach = new int[n];
        reach[0] = 1;

        for (int i=1; i<n; i++) {
            if (i >= minJump) {
                sum += reach[i-minJump];
            }
            if (i > maxJump) {
                sum -= reach[i-maxJump-1];
            }
            reach[i] = (sum > 0 && s.charAt(i) == '0') ? 1 : 0;
        }

        return reach[n-1]==1 ? true : false;
    }
}