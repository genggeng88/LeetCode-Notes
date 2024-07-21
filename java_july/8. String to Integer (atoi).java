class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        boolean neg = false;
        int i = 0, n = s.length();
        if (n == 0) {
            return 0;
        }
        if (s.charAt(i) == '-') {
            neg = true;
            i++;
        }
        else if (s.charAt(i) == '+') {
            i++;
        }
        if (i >= n || !Character.isDigit(s.charAt(i))){
            return 0;
        }
        
        int res = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            if (res > (Integer.MAX_VALUE - digit) / 10 ) {
                return neg ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            res = res * 10 + digit;
            i++;
        }
        return neg ? -res : res;
    }
}