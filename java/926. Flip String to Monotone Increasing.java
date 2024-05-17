class Solution {
    public int minFlipsMonoIncr(String s) {
        int len = s.length();
        int[] cnt = new int[len+1];
        int[] flip = new int[len+1];
        cnt[len] = 0;
        flip[len] = 0;

        for(int i=len-1; i>=0 ;i--){
            if(s.charAt(i) == '0'){
                cnt[i] = 1+cnt[i+1];
                flip[i] = flip[i+1];
            }
            else{
                cnt[i] = cnt[i+1];
                flip[i] = Math.min(cnt[i+1], 1+flip[i+1]);
            }
        }

        return flip[0];
    }
}