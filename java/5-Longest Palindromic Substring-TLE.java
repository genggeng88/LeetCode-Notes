
class Solution {
    public boolean isPalindrom(String s){
        int n = s.length();
        int i=0, j=n-1;
        while(i < j){
            if (s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public String longestPalindrome(String s) {
        if(s==null){
            return null;
        }
        int n = s.length();
        int i=0;
        String res = "";
        int length = 0;
        
        if(n==1){
            return s;
        }
        while(i<n){
            int j= n-1;
            while(i<j){
                if(s.charAt(i) == s.charAt(j) && isPalindrom(s.substring(i+1, j))){
                    String newRes = s.substring(i,j+1);
                    if(newRes.length() > length){
                        res = newRes;
                        length = newRes.length();
                    }
                }
                j--;
            }
            i++;
        }
        if(length == 0){
            return s.substring(0,1);
        }
        return res;
    }

}