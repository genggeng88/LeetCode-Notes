class Solution {
    public String licenseKeyFormatting(String s, int k) {
        s = s.replace("-", "");
        char[] chars = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        
        int i = chars.length - 1;
        while (i >= 0) {
            int j = k;
            while (i >= 0 && j > 0) {
                sb.append(chars[i]);
                i--;
                j--;
            }
            if (j == 0 && i >= 0) {
                sb.append('-');
            }
        }
        return sb.reverse().toString().toUpperCase();
    }
}