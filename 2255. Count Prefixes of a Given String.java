class Solution {
    public int countPrefixes(String[] words, String s) {
        int cnt = 0;

        for(String word : words){
            if(isPrefix(word, s)){
                cnt++;
            }
        }
        return cnt;
    }

    public boolean isPrefix(String word, String s){
        int len1 = word.length();
        int len2 = s.length();
        if(len1 > len2){
            return false;
        }
        for(int i = 0; i<len1; i++){
            if(word.charAt(i) != s.charAt(i)){
                return false;
            }
        }
        return true;
    }
}