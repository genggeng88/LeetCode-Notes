class Solution {
    public String longestCommonPrefix(String[] strs) {
        int len = strs[0].length();
        int n = strs.length;
        String shortest = strs[0];
        for (String str : strs) {
            if (str.length() < len){
                shortest = str;
                len = str.length();
            }
        }
        if (len < 1 || shortest == "") {
            return "";
        }
        for (int i=0; i<len; i++) {
            char c = shortest.charAt(i);
            for (int j=0; j<n; j++) {
                if (strs[j].charAt(i) != c) {
                    return shortest.substring(0, i);
                }
            }
        }
        return shortest;
    }
}