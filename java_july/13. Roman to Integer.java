class Solution {
    public int romanToInt(String s) {
        int n = s.length();
        int res = 0;
        for (int i=0; i<n; i++) {
            switch(s.charAt(i)){
                case 'I':
                    if (i+1 < n && (s.charAt(i+1)=='V' || s.charAt(i+1)=='X')){
                        res -= 1;
                    } else {
                        res += 1;
                    }
                    break;
                case 'X':
                    if (i+1 < n && (s.charAt(i+1)=='L' || s.charAt(i+1)=='C')){
                        res -= 10;
                    } else {
                        res += 10;
                    }
                    break;
                case 'C':
                    if (i+1 < n && (s.charAt(i+1)=='D' || s.charAt(i+1)=='M')){
                        res -= 100;
                    } else {
                        res += 100;
                    }
                    break;
                case 'V':
                    res += 5;
                    break;
                case 'L':
                    res += 50;
                    break;
                case 'D':
                    res += 500;
                    break;
                case 'M':
                    res += 1000;
                    break;
            }
        }
        return res;
    }
}