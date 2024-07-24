class Solution {
    public void rotate(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int i=0, j=m-1;

        while (i < j) {
            int[] tmp = matrix[j];
            matrix[j] = matrix[i];
            matrix[i] = tmp;
            i++;
            j--;
        }
        
        for (i=0; i<m; i++) {
            for (j=i+1; j<n; j++) {
                if (i != j) {
                    int tmp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = tmp;
                }
            }
        }
    }
}