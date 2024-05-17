class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        int cyc = 2*numRows - 2;
        int len = s.length();
        int numCols = len/cyc * (numRows-1);
        String res = "";
        if(len%cyc <= numRows){
            numCols++;
        }
        else{
            numCols = numCols + 1 + (len%cyc - numRows);
        }

        char[][] mat = new char[numRows][numCols];
        int ptr = 0;
        for(int j=0; j<numCols; j++){
            for(int i=0; i<numRows; i++){
                // for vertical column
                if(j%(numRows-1) == 0){
                    if(ptr < len){
                        mat[i][j] = s.charAt(ptr);
                        ptr++;
                    }
                }
                else if(i>0 && i< numRows-1 && i + j%(numRows-1) == numRows-1){
                    mat[i][j] = s.charAt(ptr);
                    ptr++;
                }
                else{
                    mat[i][j] = '0';
                }
            }
        }
        for(int i = 0; i<numRows; i++){
            for(int j=0; j<numCols; j++){
                if((int)mat[i][j] != 0 && mat[i][j] != '0'){
                    res = res+mat[i][j];
                }
            }
        }
        return res;
    }
}