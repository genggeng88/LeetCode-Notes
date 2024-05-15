class Solution {
    public boolean isAnagram(String s, String t) {
        int ns = s.length();
        int nt = t.length();
        if(ns != nt){
            return false;
        }
        int[] cmp = new int[26];
        
        for (int i = 0; i<ns; i++){
            cmp[s.charAt(i)-'a']++;
            cmp[t.charAt(i)-'a']--;
        }
        for(int i=0; i<26; i++){
            if(cmp[i] != 0){
                return false;
            }
        }
        return true;
    }
}