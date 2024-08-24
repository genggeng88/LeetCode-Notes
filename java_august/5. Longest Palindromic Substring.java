class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int cnt = 1;
        String res = s.substring(0,1);

        if (n == 1) {
            return res;
        }
        if (n == 2){
            if (s.charAt(0) == s.charAt(1)) {
                return s;
            }
            return res;
        }

        boolean[][] store = new boolean[n][n];

        for (int i=0; i<n-1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                store[i][i+1] = true;
                if (cnt < 2) {
                    cnt = 2;
                    res = s.substring(i, i+2);
                }
            }
            store[i][i] = true;
        }
        store[n-1][n-1] = true;

        for (int j=2; j<n; j++) {
            for (int i=0; i<j-1; i++) {
                if (s.charAt(i) == s.charAt(j) && store[i+1][j-1]) {
                    store[i][j] = true;
                    if (cnt < j-i+1) {
                        cnt = j-i+1;
                        res = s.substring(i, j+1);
                    }
                }
            }
        }

        return res;
    }
}