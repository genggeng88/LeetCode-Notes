class Solution {
    public int reverse(int x) {
        int res = 0, remain = 0;
        
        while(x != 0){
            remain = x%10;
            x = x/10;
            if(res > Integer.MAX_VALUE/10 || (res == Integer.MAX_VALUE && remain > 7)){
                return 0;
            }
            if(res < Integer.MIN_VALUE/10 || (res == Integer.MIN_VALUE && remain < -8)){
                return 0;
            }
            res = res*10 + remain;
        }
        return res;
    }
}