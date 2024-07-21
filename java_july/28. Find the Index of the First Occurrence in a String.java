class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), k = needle.length();
        int i = 0;
        while (i <= n-k) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                if (haystack.substring(i, i+k).equals(needle)) {
                    return i;
                }
            }
            i++;
        }
        return -1;
    }
}