class Solution {
    public int[] diStringMatch(String s) {
        int n = s.length(), inc=0, dec=n;
        int[] perm = new int[n+1];
        for(int i = 0; i<n; i++){
            if(s.charAt(i) == 'I'){
                perm[i] = inc;
                inc++;
            }
            else{
                perm[i] = dec;
                dec--;
            }
        }
        perm[n] = dec;
        return perm;
    }
}