class Solution {
    public boolean isAnagram(String s, String t) {
        int ns = s.length();
        int nt = t.length();
        if(ns != nt){
            return false;
        }
        char[] cs = s.toCharArray();
        char[] ct = t.toCharArray();
        Arrays.sort(cs);
        Arrays.sort(ct);

        return Arrays.equals(cs, ct);
    }
}