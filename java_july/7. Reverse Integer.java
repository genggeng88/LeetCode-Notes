class Solution {
    public int reverse(int x) {
        boolean flag = (x < 0);
        x = Math.abs(x);
        int res = 0;
        
        while (x > 0 ){
            int digit = x % 10;
            if (res > (Integer.MAX_VALUE - digit) / 10){
                return 0;
            }
            res = res * 10 + digit;
            x = x / 10;
        }
        return flag ? -res : res;
    }
}