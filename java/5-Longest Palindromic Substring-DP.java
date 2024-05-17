
class Solution {
    public String longestPalindrome(String s) {
        if(s==null){
            return null;
        }
        int n = s.length();
        if(n==1){
            return s;
        }
        boolean[][] dp = new boolean[n][n];
        //initialize dp
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i == j){
                    dp[i][j] = true;
                }
                if(i == j-1){
                    dp[i][j] = s.charAt(i)==s.charAt(j);
                }
            }
        }
        //fill up dp
        for(int i=n-3; i>=0; i--){
            for (int j=n-1; j>i+1; j--){
                if(dp[i+1][j-1]){
                    dp[i][j] = s.charAt(i)==s.charAt(j);
                }
                else{
                    dp[i][j] = false;
                }
            }
        }
        //find longest palindormic
        int resi=0, resj=0, length=1;
        for(int i=0; i<n; i++){
            for(int j=n-1; j>i; j--){
                if(dp[i][j] && j-i+1>length){
                    resi = i;
                    resj = j;
                    length = j-i+1;
                }
            }
        }
        return s.substring(resi, resj+1);
    }
}