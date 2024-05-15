class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int m = image.length, n = image[0].length;
        int[][] res = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=n-1; j>=0; j--){
                if(image[i][j] == 0){
                    res[i][n-j-1] = 1;
                }
                else{
                    res[i][n-j-1] = 0;
                }
            }
        }

        return res;
    }
}